from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from django.views import View 

from .models import DistrictChoices,BatchChoices,CourseChoices,TrainerChoices

from .utility import get_admission_number,get_password

from .models import Students

from .forms import StudentRegisterForm

from django.db.models import Q

from authentication.models import Profile

from django.db import transaction

# from django.contrib.auth.models import U

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

class GetStudentObject:
    
    def get_student(self,request,uuid):
        
        try:
            
            student = Students.objects.get(uuid=uuid)
            
            return student
            
        except:
            
            return render(request,"errorpages/error-404.html")
        
        
# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')
class DashboardView(View):
    
    def get(self,request,*args,**kwargs):
        
        # if request.user.is_authenticated:
            
            
        
        return render(request,'students/dashboard.html')
 
# roles Sales,Admin,Trainer,Accademic Counsellor 

@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Accademic Counsellor']),name='dispatch')   
class StudentsListView(View):
    
    def get(self,request,*args,**kwargs):
        
        query = request.GET.get('query')
        
        role = request.user.role
        
        if role in ['Trainer']:
            
            students = Students.objects.filter(active_status= True,trainer__profile=request.user)
        
            if query :

                students = Students.objects.filter(Q(active_status=True)&Q(trainer__profile=request.user)&(Q(first_name__icontains=query)|Q(last_name__icontains = query)|Q(house_name__icontains=query)|
               
                            
                                                                      Q(contact_num__icontains = query)|Q(pincode__icontains = query)|Q(post_office__icontains = query)|
                                                                      
                                                                      Q(email__icontains = query)|Q(course_name__icontains = query)|Q(district__icontains = query)
                                                                     
                                                                      |Q(batch_name__icontains = query)|Q(trainer__first_name__icontains=query)))                                                       
        else:
            
            students = Students.objects.filter(active_status=True)

            if query :

                students = Students.objects.filter(Q(active_status=True)&(Q(first_name__icontains=query)|Q(last_name__icontains = query)|Q(house_name__icontains=query)|
                                                                      
                                                                      Q(contact_num__icontains = query)|Q(pincode__icontains = query)|Q(post_office__icontains = query)|
                                                                      
                                                                      Q(email__icontains = query)|Q(course_name__icontains = query)|Q(district__icontains = query)
                                                                     
                                                                      |Q(batch_name__icontains = query)|Q(trainer__first_name__icontains=query)))
        # students = Students.objects.all()
        
        
        data = {'students':students,'query':query}
        
        return render(request,'students/students.html',context=data)

# roles 
class RegisterView(View):
     
    def get(self,request,*args,**kwargs):
        
        form = StudentRegisterForm()
         
        #data = {'districts':DistrictChoices,'courses':CourseChoices,'batches':BatchChoices,'trainers':TrainerChoices,'form':form}
        # data = {'numbers':[1,2,3,4,5]}
        data = {'form':form}
          
        return render(request,"students/register.html",context=data)
    
    def post(self,request,*args,**kwargs):
        
        form = StudentRegisterForm(request.POST,request.FILES)
        
        # for error in form.errors:
            
        #     print(error)
        
        if form.is_valid():
            
            with transaction.atomic():
            
                student = form.save(commit= False)
            
                student.adm_number = get_admission_number()
            
            # student.join_date = '2025-02-05'
            
                username = student.email
            
                password = get_password()
                
                print(password)
            
                profile = Profile.objects.create_user(username=username,password=password,role='Student')
            
                student.profile = profile
            
                student.save()
            
            return redirect('students-list')#-- if there is no context
        
        else:    
            
            data = {'form':form}
            
            return render(request,'students/register.html',context=data)
        
        # form_data = request.POST
        
        # first_name = form_data.get('firstname')
        
        # last_name = form_data.get('lastname')
        
        # photo = request.FILES.get('photo')
        
        # email = form_data.get('email')
        
        # contact_number = form_data.get('contactnumber')
        
        # house_name = form_data.get('housename')
        
        # district = form_data.get('district')
        
        # post_office = form_data.get('postoffice')
        
        # pincode = form_data.get('pincode')
        
        # course = form_data.get('course')
        
        # batch = form_data.get('batch')
        
        # batch_date = form_data.get('batchdate')
        
        # trainer = form_data.get('trainer')
        
        # adm_number = get_admission_number()
        
        # join_date = '2024-08-16'
        
        # Students.objects.create(first_name=first_name,
        #                         second_name=last_name,
        #                         photo=photo,
        #                         email=email,
        #                         contact=contact_number,
        #                         house_name=house_name,
        #                         district=district,
        #                         post_office=post_office,
        #                         pincode=pincode,
        #                         course=course,
        #                         batch=batch,
        #                         batch_date=batch_date,
        #                         trainer_name=trainer,
        #                         adm_number=adm_number,
        #                         join_date=join_date
        #                         )
        
        # print(first_name,last_name,photo,email,contact_number,house_name,district,post_office,pincode,course,batch,batch_date,trainer)
#student detail view 

@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Accademic Counsellor']),name='dispatch')       
class StudentDetailView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        
        #student = get_object_or_404(Students,pk=pk)
        # try:
        
        #     student = Students.objects.get(pk=pk)
            
        #     print(student)
        
        # except:
            
        #     return redirect('error-404')
        
        student = GetStudentObject().get_student(request,uuid)
        
        data = {'student':student}
        
        return render(request,'students/student-detail.html',context=data)
    
    #error 404 view
    
# class Error404View(View):
        
#     def get(self,request,*args,**kwargs):
        
#         return render(request,"students/error-404.html")
    
#     # student delete View
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')    
class StudentDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        # try:
            
        #     student = Students.objects.get(pk=pk)
            
        # except:
            
        #     return redirect('error-404')
        
        student = GetStudentObject().get_student(request,uuid)
        
        # student.delete()
        
        student.active_status = False
        
        student.save()
        
        return redirect('students-list')
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')    
class StudentUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(request,uuid)
        
        form = StudentRegisterForm(instance=student)
        
        data = {'form':form}
        
        return render(request,'students/student-update.html',context=data)
    
    def post(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        
        student = GetStudentObject().get_student(request,uuid)
        
        form = StudentRegisterForm(request.POST,request.FILES,instance=student)        
        
        if form.is_valid():
            
            form.save()
            
            return redirect('students-list')
        
        else:
            
            data = {'form':form}
            
            return render(request,"students/student-update.html",context=data)
        

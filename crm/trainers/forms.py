from django import forms

from .models import Trainers,DistrictChoices

from batches.models import Batches

from trainers.models import Trainers

from courses.models import Courses

class TrainersRegisterForm(forms.ModelForm):
    
    class Meta:
        
        model = Trainers
    
        # fields=['first_name','second_name','photo','email','contact','house_name','post_office','district','pincode','mark','course','batch','batch_date','trainer_name']
        
        # if all fields in the model are used, give fields = '__all__'
        
        exclude = ['uuid','active_status','profile',"employee_id"]
        
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'last_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'photo':forms.FileInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                
                                                }),
            'email':forms.EmailInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'contact':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'house_name':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'post_office':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'pincode':forms.TextInput(attrs={'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                # 'placeholder':'Enter first name',
                                                'required':'required',
                                                }),
            'qualification' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter qualification', 
                                                                    'required' :'required'}),
            'stream' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter stream', 
                                                                    'required' :'required'}),
            'id_card' : forms.FileInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                   'required':'required'}),
        }
    
    district = forms.ChoiceField(choices=DistrictChoices.choices,widget=forms.Select(attrs={
        'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
        'required':'required'}))
    
    # course = forms.ChoiceField(choices=CourseChoices.choices,widget=forms.Select(attrs={
    #     'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #     'required':'required'}))
    
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={
        'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
        'required':'required'}))
    
    # batch = forms.ChoiceField(choices=BatchChoices.choices,widget=forms.Select(attrs={
    #     'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #     'required':'required'}))
    
    # batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(attrs={
    #     'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #     'required':'required'}))
    
    # trainer_name = forms.ChoiceField(choices=TrainerChoices.choices,widget=forms.Select(attrs={
    #     'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
        # 'required':'required'}))
        
    # trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(attrs={
    #     'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #     'required':'required'}))
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        pincode = cleaned_data.get('pincode')
        
        email = cleaned_data.get('email')
        
        # if Trainers.objects.filter(profile__username=email).exists():
            
        #     self.add_error('this email is already registered. please change email')
        
        if len(pincode)<6:
            
            self.add_error('pincode','pincode must be 6 digits')
        
        return cleaned_data
        
    
def __init__(self,*args,**kwargs):
    
    super(TrainersRegisterForm,self).__init__(*args,**kwargs)
    
    if not self.instance:
        
        self.fields.get('photo').widget.attrs['required'] = 'required'
# cron to senf remainder email about payment

from .models import Payment

from django.utils import timezone

import threading

from students.utility import send_email

from apscheduler.schedulers.background import BackgroundScheduler

def email_remainder():
    
    current_date = timezone.now().date()
    
    five_days_before_date = current_date-timezone.timedelta(days=5)
    
    pending_payments = Payment.objects.filter(status='Pending',student__join_date__lte=five_days_before_date)
    
    if pending_payments.exists():
        
        # sending payment remainder to student through email
        
        for payment in pending_payments:
        
            subject = 'Payment Remainder'
                    
            # sender = settings.EMAIL_HOST_USER
            
            recepient = [payment.student.email]
            
            template = 'email/payment-remainder.html'
            
            context = {'name':f'{payment.student.first_name} {payment.student.second_name}'}
                
            # send_email(subject,recepient,template,context)
            
            thread = threading.Thread(target=send_email,args=(subject,recepient,template,context))
            
            thread.start()
            
            print("all email sent")


def scheduler_start():
    
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(email_remainder,'cron',hour=10,minute=0)
    
    scheduler.start()
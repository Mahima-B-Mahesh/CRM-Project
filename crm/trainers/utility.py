import uuid

from .models import Trainers

import string

import random

def get_employee_id():
    
    while True:
    
        pattern = str(uuid.uuid4().int)[:2]
    
        employee_num = f'LM-E{pattern}'
        
        if not Trainers.objects.filter(employee_id=employee_num).exists():
            
            return employee_num
    
    
    
# get_admission_number()

def get_password():
        
    password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))
    
    return password
    
get_password()
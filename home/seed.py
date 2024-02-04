from faker import Faker
import random
fake = Faker()
from .models import *

def seed_db(n=100):
    try:
        for i in range(0,n):
            department_objs = Department.objects.all()
            random_index = random.randint(0,len(department_objs)-1)
            department = department_objs[random_index]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,30)
            student_address = fake.address()

            studentid_obj = StudentId.objects.create(student_id = student_id)
            student_obj = Student.objects.create(
                department = department,
                student_id = studentid_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)
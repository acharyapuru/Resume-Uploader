from django.db import models

STATES=(
    ('KOSHI','Koshi'),
    ('MADHESH','Madhesh'),
    ('BAGMATI','Bagmati'),
    ('LUMBINI','Lumbini'),
    ('KARNALI','Karnali'),
    ('SUDURPASCHIM','Sudurpaschim')
)

class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(max_length=50,choices=STATES)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)


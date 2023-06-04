from django import forms 
from .models import Resume

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)
JOB_CITY_CHOICES=(
    ('KTM','Kathmandu'),
    ('Lalitpur','Lalitpur'),
    ('Chitwan','Chitwan'),
    ('Biratnagar','Biratnagar'),
    ('Birtamod','Birtamod'),
    ('PKR','Pokhara'),
    ('JNP','Janakpur')
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels={
            'name':'Full Name',
            'dob':'Date of Birth',
            'pin':'Pin Code',
            'mobile':'Mobile No',
            'email':'Email',
            'profile_image':'Profile Image',
            'my_file':'Document'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','type':'phone'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

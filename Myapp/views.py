from django.shortcuts import render,redirect
from Myapp.forms import ResumeForm
from .models import Resume
from django.contrib import messages

from django.views import View

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'home.html',{'form':form,'candidates':candidates})
    
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
         form.save()
         return redirect('home')
        

class CandidateView(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request,'profile.html',{'candidate':candidate})
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request,'Index.html')
 
def aboutme(request):
  return render(request,'Aboutme.html')

def experience(request):
  return render(request,'Experience.html')

def project(request):
  return render(request,'project.html')
from django.shortcuts import render
from django.contrib import messages 
from .models import Contact

# Create your views here.
def home(request):
    context={'HomeActive':'active'}
    return render(request, 'home.html',context)

def services(request):
    context={'ServiceActive':'active'}
    return render(request, 'services.html',context)

def skill(request):
    context={'SkillActive':'active'}
    return render(request, 'skill.html',context)

def contact(request):
    context={'ContactActive':'active'}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent. Thank you!")
    return render(request, 'contact.html',context)


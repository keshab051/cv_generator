from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# def accept(request):
#     form= movie_list(request.POST)
#     form.save()

#     # if request.method =="POST":
#     #     name = request.POST.get("name","")
#     #     email = request.POST.get("email","")
#     #     phone = request.POST.get("phone","")
#     #     summary = request.POST.get("summary","")
#     #     degree = request.POST.get("degree","")
#     #     school = request.POST.get("school","")
#     #     university = request.POST.get("university","")
#     #     previous_work = request.POST.get("previous_work","")
#     #     skills = request.POST.get("skills","")

#     #     profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
#     #     profile.save()
#     return render(request,'pdf/accept.html')

# Create your views here.


def accept(request):      
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accept')  
    else:
        form = ProfileForm()
    return render(request, 'pdf/accept.html', {'form': form})

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options={
            'page-size':'Letter',
            'encoding':"UTF-8"
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['content-Disposition']='attachment'
    filename = "resume.pdf"
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})
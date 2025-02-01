from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm

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

from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from poll_app.models import Candidates


# Create your views here.
def home(request):
  # check if the user is login in
     if request.method == "POST":
         fullname = request.POST["fullname"]
         card_id = request.POST["card_id"]
         user = authenticate(request, username=fullname, password=card_id)
         if user is not None:
             login(request, user)
             messages.success(request, f"{fullname}You can vote now 😎 ")
             return redirect("vote")
         else:
             messages.error(request, "There is error please login in again")
             return redirect("home")
     else:
         return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    #messages.success(request, message="You have been logout successfully. see you again ")
    return  redirect("home")

def vote(request):
    candidate = Candidates.objects.all()
    return  render(request, 'voting_page.html', {"candidate": candidate} )

def hero(request):
    return  render(request, 'landingpage.html', {} )






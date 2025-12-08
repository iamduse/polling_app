from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages


# Create your views here.
def home(request):
     #return render(request, 'index.html', {})
  # check if the user is login in
     if request.method == "POST":
         email = request.POST["email"]
         password = request.POST["password"]
         user = authenticate(request, username=email, password=password)
         if user is not None:
             login(request, user)
             messages.success(request, "Successfully Login In. Now You can VoteVote 😎 ")
             return redirect("home")
         else:
             messages.error(request, "There is error please login in again")
             return redirect("login")
     else:
         return render(request, 'login.html', {})




def user_login(request):
    pass





def user_logout(request):
    logout(request)
    messages.success(request, message="You have been logout successfully. see you again ")
    return  redirect("home")
from django.contrib.messages import success
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from poll_app.models import Candidates, Vote


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

    return  redirect("home")

def vote(request):
    candidates = Candidates.objects.all()

    if request.method == "POST":
        # 1. Check if user is logged in
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to vote.")
            return redirect('login')

        # 2. Check if user already voted
        if Vote.objects.filter(user=request.user).exists():
            messages.error(request, "You have already voted.")
            return redirect('vote')

        # 3. Get candidate ID from form
        candidate_id = request.POST.get("candidate_id")
        selected_candidate = get_object_or_404(Candidates, id=candidate_id)

        # 4. Save vote
        Vote.objects.create(
            user=request.user,
            candidate=selected_candidate
        )

        # 5. Increase candidate vote count
        selected_candidate.votes += 1
        selected_candidate.save()

        # 6. Success message
        messages.success(
            request,
            f"You voted for {selected_candidate.name} successfully!"
        )

        return redirect('vote')

    return render(request, 'voting_page.html', {"candidate": candidates})




def hero(request):
    return  render(request, 'landingpage.html', {} )








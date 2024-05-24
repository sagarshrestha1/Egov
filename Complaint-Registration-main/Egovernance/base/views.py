from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from .forms import LoginForm,RegistrationForm,ComplaintForm
from django.contrib.auth.decorators import login_required
from .models import Complaint
# Create your views here.
def home(request):
    return render(request,'base/home.html')
def signup(request):
    return render(request,"base/signup.html")

def login_view(request):
    form = LoginForm()  # Create an instance of the form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Corrected: Return redirect response
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)  # Logs the user out
    messages.success(request, "You have been logged out successfully.")  # Add success message
    return redirect("home")
def signup(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.username=user.username.lower()
            user.save()
            messages.success(request,'Account created and Logged In successfully.')
            login(request,user)
            return redirect('home')
        else:
            return render(request,"registration/sign-up.html",{
                                        "form":form
                                            })
    else:
        form=RegistrationForm()
        return render(request,"registration/sign-up.html",{
                                        "form":form
                                            })
def view_complaint(request):
    complaint=Complaint.objects.all()
    print(complaint)
    return render(request,'base\complaints.html',{
        "complaint":complaint,
    })
@login_required
def register_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your complaint has been registered successfully.')
            return redirect('view')
    else:
        form = ComplaintForm()
    return render(request, 'base/add_complaint.html', {'form': form})
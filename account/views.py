from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


## LOGIN FUNCTION
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['username'], password= cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated','Successful')
                else:
                    return HttpResponse('Account not active')
            else:
                return HttpResponse('Invalid Account')
    else:
        form: LoginForm()

    template_name = 'account/login.html'
    context = {
        'form':form,
    }
    return render(request,template_name,context)
    
## Registration Form
def register(request):
    user_form = UserRegistrationForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
        new_user.set_password(
            user_form.cleaned_data['password']
        )
        new_user.save()
        return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    template_name = 'account/register.html'
    context = {
        'user_form':user_form,
    }
    return render(request,template_name,context)



##login_required
@login_required
def dashboard(request):
    section = 'dashboard'
    template_name = 'account/dashboard.html'
    context = {
        'section':section,
    }
    return render(request,template_name,context)



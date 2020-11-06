from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
# Create your views here.


### LOGIN FUNCTION
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
    

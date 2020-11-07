from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
# Create your views here.

@login_required
def image_create(request):
    # form = ImageCreateForm(data=request.GET)
    if request.method == 'POST':
        form = ImageCreateForm(data= request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request,'Image Uploaded Successfully')
            return redirect(new_item.get_absolute_url())
        
        else:
            form = ImageCreateForm(data=request.GET)
    else:
        form = ImageCreateForm(data=request.GET)
    template_name = 'images/create.html'
    return render(request,template_name,{'section':'images','form':form})


def imaage_detail(request,id,slug):
    images = get_object_or_404(Image,id=id,slug=slug)
    template_name = 'images/detail.html'
    context = {
        'image':images,
    }
    return render(request,template_name,context)

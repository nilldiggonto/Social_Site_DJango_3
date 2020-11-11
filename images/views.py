from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,3)
    page = request.GET.get('page')

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)

    template_name = 'images/list.html'

    context = {
        'images':images,
        
    }
    return render(request,template_name,context)




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



############## AJAX
@login_required
@require_POST
@ajax_required
def image_like(request):
    img_id      = request.POST.get('id')
    action      = request.POST.get('action')

    if img_id and action:
        try:
            image = Image.objects.get(id='img_id')
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})
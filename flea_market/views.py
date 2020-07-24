from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .models import *
from .forms import *
from portfolio import settings


def index(request):
    categories = SectionProduction.objects.filter(type_category__exact=SectionProduction.CATEGORY)
    print(categories.count())
    return render(request, 'flea_market/flea_market_index.html', {
        'categories': categories,
        'user': request.user,
    })


def products(request, number_cat):
    print('numb cat {}'.format(number_cat))
    return render(request, 'flea_market/flea_market_products.html')


def detail(request, ad_id):
    return HttpResponse('Ad number {}'.format(ad_id))


def check_login(request):
    if request.method == 'GET':
        return render(request, 'flea_market/login.html', {
            'user': request.user,
        })
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_path = request.META.get('HTTP_REFERER').split('?next=')
                if len(redirect_path) > 1:
                    return redirect(redirect_path[1])
                else:
                    return redirect(reverse("flea_market:index"))
            else:
                print('disabled account')
        else:
            return redirect(request.META.get('HTTP_REFERER'))


@login_required
def add_ad(request):
    # to do post
    return render(request, 'flea_market/new_post.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'flea_market/registration.html')
    elif request.method == 'POST':
        # to do errors uniq user data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email, password)
        return redirect(reverse('flea_market:login'))


# def upload_ad(request):
#     if request.method == 'POST':
#         form_user = UserForm()
#         form_img = UploadImageForm(request.POST, request.FILES)
#         form_ad = AdForm()
#
#         print(request.FILES['photo'])
#         if form_img.is_valid():
#             instance = UserImage(photo=request.FILES['photo'])
#             instance.save()
#             return render(request, 'flea_market/upload.html', {
#                 'form_img': form_img,
#             })
#
#         return render(request, 'flea_market/upload.html', {
#             'form_user': form_user,
#             'form_ad': form_ad,
#             'form_img': form_img,
#         })
#     else:
#         form_user = UserForm()
#         form_ad = AdForm()
#         form_img = UploadImageForm()
#         return render(request, 'flea_market/upload.html', {
#             'form_user': form_user,
#             'form_ad': form_ad,
#             'form_img': form_img,
#         })

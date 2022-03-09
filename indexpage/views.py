
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import CreateView, DeleteView, ListView
from .models import IntroduceUs, WhatWeDo, PhotosTitle, PhotosTitle_Photos, Publications
from django.views import generic
# Create your views here.


def index(request):
    p = IntroduceUs.objects.all()[:4]
    picture_first = PhotosTitle_Photos.objects.all()[:1]
    picture = PhotosTitle_Photos.objects.all()[1:]
    pubilction = Publications.objects.all()[:3]
    what_we_do = WhatWeDo.objects.all()

    return render(request, 'indexpage/index.html', context={'obj': p, 'obj_pic': picture, 'obj_pic_first': picture_first, 'obj_pubilction': pubilction, 'obj_what_we_do': what_we_do})


def about_professor(request):
    p = IntroduceUs.objects.get(category='Professor')
    j = IntroduceUs.objects.filter(category='Research Collaborators')

    return render(request, 'indexpage/about.html', context={'data': p, 'Coll': j})


def what_we_do(request):
    p = WhatWeDo.objects.all()
    return render(request, 'indexpage/service.html', context={'data': p})


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class customHandler(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, "indexpage/404.html")


def introduce(request):
    p = IntroduceUs.objects.all()
    return render(request, 'indexpage/team.html', context={'data': p})


def pubilcation(request):
    p = Publications.objects.all()

    return render(request, 'indexpage/testimonial.html', context={'data': p})


def contact_us(request):
    return render(request, 'indexpage/contact.html')

from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# from django.http import HttpResponse


# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = ' BASIC INJECTION! '
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basicapp/school_detail.html'

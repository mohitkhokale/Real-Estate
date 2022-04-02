from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from property.forms import EnquiryForm
from . models import Enquiry, Property

# Create your views here.
class PropertiesViews(View):
    
    def get(self,request,property_id=None):
        search = request.GET.get('search', None)
        search_prop = ''
        context={}
        data = Property.objects.filter()
        if search:
            data = Property.objects.filter(prop_name__icontains = search)
            search_prop = Property.objects.filter(prop_name__icontains = search)
            context = {
                'data': data,
                'search_prop':search_prop
            }
        else:
            context = {
                'data': data,
            }
            return render(request,'properties.html',context)
        return render(request,'properties.html',context)


class PropertyViews(View):
    def get(self, request,property_id=None):
        data = Property.objects.filter(pk=property_id)
        search = request.GET.get('search', None)
        search_prop = ''
        context={}
        if search:
            search_prop = Property.objects.filter(prop_name__icontains = search)
            context = {
                'data': data,
                'search_prop':search_prop
            }
        else:
            context = {
                'data': data,
            }
            return render(request,'property.html',context)
        return render(request,'properties.html',context)


class EnquiryView(View):
    template_name = 'enquiry.html'
    form_class = EnquiryForm

    def get(self, request):
        form_class = self.form_class()
        form = Enquiry.objects.filter()
        enquiry = Enquiry.objects.filter(user_id=request.user.id)
        # print(enquiry)
        if form_class.is_valid():
            form_class.save()
        context = {
            'form_class': form_class,
            'forms': form,
            'enquiry':enquiry
        }

        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

def Deletedata(request,id=None):
    Enquiry.objects.filter(id=id).delete()
    return redirect('index')

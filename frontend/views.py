from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from property.models import Enquiry, Property
# Create your views here.

class HomePage(View):
    def get(self, request,property_id=None):
    
        data = Property.objects.filter()
        enquiry = Enquiry.objects.filter(user_id=request.user.id)
        search = request.GET.get('search')
        search_prop = ''
        context={}
        if search:
            data = Property.objects.filter(prop_name__icontains=search)
            search_prop = Property.objects.filter(prop_name__icontains=search)
            print("search",search_prop)
            context = {
            'data': data,
            'enquiry':enquiry,
            'search_prop': search_prop,

            }
        else: 
            context = {
            'data': data,
            'enquiry':enquiry,
            'search_prop': search_prop,

            }  
            return render(request,'index.html',context)

        return render(request,'properties.html',context)
  

def Contact(request):
    return render(request,'contact.html')
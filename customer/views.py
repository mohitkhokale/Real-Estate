from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout , authenticate

from customer.forms import SignUpForm
 
# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    form_class = AuthenticationForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request,self.template_name, context)

    def post(self,request):
        form = self.form_class( data =request.POST or None)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('index')
        context= {
            'form':form,
        }
        return render(request,self.template_name, context)

def LogoutView(request):
    logout(request)
    return redirect('index')
 
def RegisterView(request):


    form = SignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.UserProfile.first_name = form.cleaned_data.get('first_name')
        user.UserProfile.last_name = form.cleaned_data.get('last_name')
        user.UserProfile.email = form.cleaned_data.get('email')
        user.UserProfile.mobile = form.cleaned_data.get('mobile')
        user.UserProfile.about = form.cleaned_data.get('about')
        user.UserProfile.dob = form.cleaned_data.get('dob')
        user.UserProfile.address = form.cleaned_data.get('address')
        user.UserProfile.user_img = form.cleaned_data.get('user_img')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'forms': form})
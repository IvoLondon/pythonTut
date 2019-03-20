from django.shortcuts import render
from basicform.forms import FormName
from basicform.admin_forms import UserForm, UserProfileInfoForm

 from django.contrib.auth import authenticate, login, logout
 from django.http import HttpResponseRedirect, HttpResponse
 from django.core.urlresolvers import reverse
 from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basicform/index.html')


def form_name_view(request):
    form = FormName()
    details = {
        'title': 'form page',
        'number': 1000,
    }

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print('VALIDATION PASSED')
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])
            return index(request)
    return render(request, 'basicform/form_page.html', {'form': form,
                                                        'details': details})


def form_admin_view(request):

    registered = False
    
    if request.method == 'POST':
        users_form = UserForm(data=request.POST)
        user_profile = UserProfileInfoForm(data=request.POST) 

        if users_form.is_valid() and user_profile.is_valid():

            user = users_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(users_form.errors, user_profile.errors)
    else:
        users_form = UserForm()
        user_profile = UserProfileInfoForm()

    return render(request, 'basicform/form_admin.html', {
                                                'users_form': users_form,
                                                'user_profile': user_profile,
                                                'registered': registered
                                                })

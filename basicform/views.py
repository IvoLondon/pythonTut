from django.shortcuts import render
from basicform.forms import FormName
from basicform.admin_forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here. 
def index(request):
    return render(request, 'basicform/index.html')


@login_required
def special(request):
    return HttpResponse('You are logged in, nice!')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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

            user = users_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user
            import pdb; pdb.set_trace()
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACOUNT NOT ACTIVE')
        else:
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'basicform/login.html', {})

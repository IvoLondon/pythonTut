from django.shortcuts import render
from basicform.forms import FormName


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
    return render(request, 'basicform/form_page.html', {'form': form, 'details' : details})
   
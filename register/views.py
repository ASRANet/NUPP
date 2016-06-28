from django.shortcuts import render
from register.forms import UserForm
from mainApp.models import SiteSetting


def index(request):

    site_settings = SiteSetting.objects.all().first()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'register/successPage.html', {'site_settings': site_settings})

        else:
            print form.errors
    else:
        form = UserForm()

    return render(request, 'register/register.html', {'form': form, 'site_settings': site_settings})


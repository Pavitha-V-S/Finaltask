from django.shortcuts import render, redirect
import json
from django.contrib.auth import authenticate,login
from .models import District, SubArea, Branch, AccountType, Customer, Material
from .forms import RegistrationForm, AdditionalInfoForm, LoginForm, WikipediaForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('application_form')
            else:
                form.add_error(None, "Invalid username or password.")

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application_form')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def application_form(request):
    districts = District.objects.all()
    branches = {}
    for district in districts:
        branches[district.id] = list(district.branch_set.values("id", "name"))

    materials = Material.objects.all()

    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            # customer.materials_provide.set(form.cleaned_data['materials_provide'])

            customer.save()
            form.save_m2m()

            message = "Application accepted"
            return render(request, 'message_page.html', {'message': message})
    else:
        form = AdditionalInfoForm()

    return render(request, 'application_form.html',
                  {'form': form, 'districts': districts, 'branches_json': json.dumps(branches), 'materials': materials})

def wikipedia_redirect(request, district):
    wikipedia_urls = {
        'Thiruvananthapuram': 'https://en.wikipedia.org/wiki/Thiruvananthapuram',
        'Kollam': 'https://en.wikipedia.org/wiki/Kollam',
        'Ernakulam': 'https://en.wikipedia.org/wiki/Ernakulam',
        'Alappuzha': 'https://en.wikipedia.org/wiki/Alappuzha',
        'Thrissur': 'https://en.wikipedia.org/wiki/Thrissur',

    }

    if district in wikipedia_urls:
        return redirect(wikipedia_urls[district])
    else:
        return redirect('bankapp:home')

# def wikipedia(request, district_name):
#     district = District.objects.get(name=district_name)
#     wikipedia_url = district.wikipedia_url
#     return redirect(wikipedia_url)

# def wikipedia(request):
#     if request.method == 'POST':
#         selected_district = request.POST.get('district')
#         district = District.objects.get(name=selected_district)
#         wikipedia_url = district.wikipedia_url
#         return render(request, 'wikipedia.html', {'districts': District.objects.all(), 'wikipedia_url': wikipedia_url})
#
#     return render(request, 'wikipedia.html', {'districts': District.objects.all()})

def message_page(request):
    message = "Application accepted"
    return render(request, 'message_page.html', {'message': message})

def logout(request):
    # logout(request)
    return render(request, 'logout.html')
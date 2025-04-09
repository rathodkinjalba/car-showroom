from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import person
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index1.html')
def index(request):
    return render(request,'index2.html')
def EVIRATA(request):
    return render(request,'EVIRATA1.html')
def FRONX(request):
    return render(request,'FRONX2.html')
def INVICTO(request):
    return render(request,'INVICTO3.html')
def JIMNY(request):
    return render(request,'JIMNY4.html')
def CIAZ(request):
    return render(request,'CIAZ5.html')
def BALENO(request):
    return render(request,'BALENO6.html')
def GRAND_VIRATA(request):
    return render(request,'GRAND_VIRATA7.html')
def IGNIS(request):
    return render(request,'IGNIS8.html')
def XL6(request):
    return render(request,'XL69.html')

def person_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        model = request.POST.get('model')
        color = request.POST.get('color')

        # Save to DB
        person.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city,
            model=model,
            color=color
        )
        messages.success(request, 'Inquiry submitted successfully!')
        return redirect('success')  

    return render(request, 'your_form_page.html')
def success(request):
    return render(request, 'success.html')






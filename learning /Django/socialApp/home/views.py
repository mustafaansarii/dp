from django.shortcuts import render

def index(request):
    contex={
        "variable":"this is sent"
    }
    return render(request, 'index.html', {'card_range': range(6)})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

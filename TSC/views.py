from django.shortcuts import render
from compression_middleware.decorators import compress_page
from .forms import EmailForm
from django.contrib import messages

@compress_page
def index(request):
    return render(request, 'index.html',{
    })

@compress_page
def about(request):
    return render(request, 'about.html',{
        
    })

@compress_page
def services(request):
    return render(request, 'services.html',{
        
    })

@compress_page
def contact(request):
    form = EmailForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.send_email()
        messages.success(request,'Mensaje enviado')
        form = EmailForm(None)
    elif request.method=='POST' and not form.is_valid():
        messages.error(request,'Revisa que todo este en orden')
    return render(request, 'contact.html',{
        'form':form
    })



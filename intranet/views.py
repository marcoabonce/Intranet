from django.shortcuts import render
from compression_middleware.decorators import compress_page
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from users.models import User
import pytz
from datetime import datetime
from mensajes.models import Mensaje


@compress_page
def index(request):
    if not request.user.is_authenticated:
        return redirect ('intranet:login')
    time_mx = pytz.timezone('America/Mexico_City')
    time = datetime.now(time_mx)
    mensajes = Mensaje.objects.all()
    for men in mensajes:
        print (men.title)
    saludo = "Hola"
    if int(time.strftime("%H"))>5 and int(time.strftime("%H"))<12:
        saludo = "Buenos días"
    if int(time.strftime("%H"))>11 and int(time.strftime("%H"))<20:
        saludo = "Buenas tardes"
    if int(time.strftime("%H"))>19 and int(time.strftime("%H"))<=24:
        saludo = "Buenas noches"
    if int(time.strftime("%H"))>=0 and int(time.strftime("%H"))<=5:
        saludo = "Buenas noches"
    print(time.strftime("%H"))
    
    return render(request,'intranet/index.html',{
        'user':request.user.first_name, 'saludo':saludo, 'mensajes':mensajes
    })

@compress_page
def login_view(request):
    if request.user.is_authenticated:
        return redirect ('intranet:index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user:
            user = authenticate(username=user.username, password=password)
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.first_name))
            return redirect('intranet:index')
        else:
            messages.error(request,'Credenciales incorrectas')
    return render(request,'intranet/login.html',{

    })

@compress_page
def category_view(request):
    if not request.user.is_authenticated:
        return redirect ('intranet:login')
    time_mx = pytz.timezone('America/Mexico_City')
    time = datetime.now(time_mx)
    saludo = "Hola"
    if int(time.strftime("%H"))>5 and int(time.strftime("%H"))<12:
        saludo = "Buenos días"
    if int(time.strftime("%H"))>11 and int(time.strftime("%H"))<20:
        saludo = "Buenas tardes"
    if int(time.strftime("%H"))>19 and int(time.strftime("%H"))<=24:
        saludo = "Buenas noches"
    if int(time.strftime("%H"))>=0 and int(time.strftime("%H"))<=5:
        saludo = "Buenas noches"
    print(time.strftime("%H"))
    return render(request,'intranet/category.html',{
        'user':request.user.first_name, 'saludo':saludo
    })

@compress_page
def logout_view(request):
    name = request.user.first_name
    logout(request)
    messages.success(request,'Hasta pronto {}!!!'.format(name))
    return redirect('intranet:login')
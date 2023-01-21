from django.shortcuts import render,redirect
from app.forms import RegistroForm
from app.models import Registros


# Create your views here.
def home(request):
    data = {}
    data['db'] = Registros.objects.all()
    return render (request,'index.html',data)

def form(request):
    data = {}
    data['form'] = RegistroForm
    return render(request,'form.html',data)

def create(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect('home')
    else:
        return redirect('form')


def view(request,pk):
    data = {}
    data['db'] = Registros.objects.get(pk=pk)
    return render(request,'view.html',data)

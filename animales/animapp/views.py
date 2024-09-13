from django.shortcuts import render
def rendervista(request):
    return render(request,'templates/vista.html')
# Create your views here.
def rendervista2(request):
    return render(request,'templates/vista2.html',)
def rendervista3(request):
    data={"foto1":'gato.jpg'}
    return render(request,'templates/vista2.html',data)
def rendervista4(request):
    data={"foto2":'perro.jpg'}
    return render(request,'templates/vista2.html',data)
def rendervista5(request):
    data={"foto3":'leon.jpg'}
    return render(request,'templates/vista2.html',data)

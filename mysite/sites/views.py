from django.shortcuts import render

def index(request):
    return render(request, 'sites/index.html')

def html(request):
    return render(request, 'sites/html.html')

def css(request):
    return render(request, 'sites/css.html')

def javascript(request):
    return render(request, 'sites/js.html')

def php_(request):
    return render(request, 'sites/php.html')

def c(request):
    return render(request, 'sites/c.html')

def cpp(request):
    return render(request, 'sites/cpp.html')

def java(request):
    return render(request, 'sites/java.html')

def py(request):
    return render(request, 'sites/python.html')

def linux(request):
    return render(request, 'sites/linux.html')

def projects(request):
    return render(request, 'sites/projects.html')
from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
    return render(request, "home.html") 

# Create your views here.
def technicalissues(request):
    return render(request, "technicalissues.html")
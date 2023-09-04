from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def home_view(request):
    # Your view logic here...
    return render(request, 'home.html', {})
from django.shortcuts import render

# Create your views here.
def escola(request):
    return render(request, 'escola.html')
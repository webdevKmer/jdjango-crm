from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'leads/home.html', context)

def leads(request):
    context = {}
    return render(request, 'leads/leads.html', context)
    
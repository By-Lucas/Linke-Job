from django.shortcuts import render

# Create your views here.
def todas_vagas(request):
    return render(request, 'todas-as-vagas.html')
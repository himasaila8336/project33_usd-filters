from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'hi how are YoU'} 
    return render(request,'filters.html',d) 
from django.shortcuts import render,redirect
from PieChart .models import Mobile

# Create your views here.
def home(request):
    return render (request,'home.html')

def Pie_Chart(request):
    labels =[]
    data=[]

    queryset = Phone.Objects.Order_by('population')[:9]
    for Mobile in queryset:
        labels.append(Mobile.name)
        data.append(Mobile.population)

    return render (request, 'Pie_Chart.html', {
         'lables': lables,
        'data' : data,
        })

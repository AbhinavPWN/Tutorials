from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'my_app/index.html')


def variable_view(request):
    my_name = {'firstname': 'abhinav'}
    context = {'my_name': my_name}
    return render(request, 'my_app/variable.html', context)

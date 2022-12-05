from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ReviewForm
# Create your views here.


def index(request):
    return render(request, 'my_app/index.html')


def variable_view(request):
    my_name = {'firstname': 'abhinav'}
    context = {'my_name': my_name}
    return render(request, 'my_app/variable.html', context)


def rental_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_app:thank_you'))
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'my_app/rental_review.html', context)


def thankyou(request):
    return render(request, 'my_app/thank_you.html')

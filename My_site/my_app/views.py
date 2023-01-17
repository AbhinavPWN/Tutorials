from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import ReviewForm, ContactForm
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from my_app.models import Teacher
# Create your views here.

thank_you = 'my_app:thank_you'
teacher_list = 'my_app:teacher_lists'


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
            return redirect(reverse(thank_you))
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'my_app/rental_review.html', context)


class ThankYouView(TemplateView):
    template_name = "my_app/thank_you.html"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'my_app/contact.html'

    # success_url
    # name of the url to be redirected
    success_url = reverse_lazy(thank_you)

    # What to do with your form
    def form_valid(self, form) -> HttpResponse:
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy(thank_you)


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teachers_name"  # by default = object_list


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy(teacher_list)


class TeacherDeleteView(DeleteView):
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy(teacher_list)

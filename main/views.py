from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from main.models import News_model_total, Comment
from main.forms import CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse


def tests(request):
    return render(request,'main/testy.html')

def test2(request):
    return render(request,'main/pilot.html')

def test3(request):
    return render(request,'main/kontakty.html')



class MainPost(ListView):
    model = News_model_total
    context_object_name = 'posts'
    template_name = 'main/home.html'
    ordering = ['-date']


class DetailPost(FormMixin,DetailView):
    model = News_model_total
    template_name = 'main/detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(DetailPost, self).form_valid(form)

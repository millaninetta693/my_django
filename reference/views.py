from django.shortcuts import render, get_object_or_404
from .models import Reference
from taggit.models import Tag 
from django.core.paginator import (Paginator,
                                    EmptyPage,
                                    PageNotAnInteger)
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

@login_required
def reference_list(request):

    object_list = Reference.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        references = paginator.page(paginator.num_pages)
        

    return render(request,
                    'reference/post/list.html',
                    {'references': references, 'page': page})

class ReferenceCreateView(LoginRequiredMixin, CreateView):
    model = Reference
    fields = ['title', 'description', 'link']
    template_name = 'reference/post/reference_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)

        return super().form_valid(form)

class ReferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Reference
    fields = ['title', 'description', 'link']
    template_name = 'reference/post/reference_form.html'
    query_pk_and_slug = True

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)
        return super().form_valid(form)

class ReferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Reference
    template_name = 'reference/post/reference_confirm_delete.html'
    success_url = reverse_lazy('reference:reference_list')
    query_pk_and_slug = True

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)

# Create your views here.

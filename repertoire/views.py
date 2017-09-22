from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .zotero import MyZotero

from .models import Oeuvre


def zotero_list(request):
    zot = MyZotero()
    zot.create_from_zotero_top(10)

    return redirect('repertoire:list_oeuvres')

class ElementList(ListView):
    model = Oeuvre
    context_object_name = 'oeuvres'
    template_name = 'oeuvres/list_page.html'


class ElementDisplay(DetailView):
    model = Oeuvre
    context_object_name = 'oeuvre'
    template_name = 'oeuvres/display.html'


class ElementEdit(UpdateView):
    model = Oeuvre
    fields = [ 'title', 'articles' ]
    template_name = 'oeuvres/edit.html'

    def get_success_url(self):
        return reverse('sp_app:display_oeuvre', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.request.user.has_perm('sp_app.change_element'):
            return super(ElementEdit, self).form_valid(form)
        else:
            return HttpResponseForbidden()

# Class based view, form
class ElementNew(CreateView):
    model = Oeuvre
    fields = [ 'title', 'articles' ]
    template_name = 'oeuvres/edit.html'

    def get_success_url(self):
        return reverse_lazy('sp_app:display_oeuvre', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.request.user.has_perm('sp_app.add_element'):
            form.instance.creator = self.request.user
            return super(ElementNew, self).form_valid(form)
        else:
            return HttpResponseForbidden()

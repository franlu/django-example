from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Card

class IndexView(generic.ListView):
    template_name = 'card/index.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return Card.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Card
    template_name = 'card/detail.html'

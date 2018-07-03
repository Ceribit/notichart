# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
from datetime import date
# Create your views here.
def home(request):
    note_list = Notes.objects.all()[:10]
    context = {
        'notes' : note_list
    }
    return render(request, 'dashboard/home.html', context)

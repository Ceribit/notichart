# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import feedparser

from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
from datetime import date
# Create your views here.
def home(request):
    note_list = Notes.objects.all()[:10]
    feeds = feedparser.parse('https://www.novelupdates.com/rss.php?uid=101502&unq=59e2dfbf49d04&type=0&lid=local')
    context = {
        'notes' : note_list,
        'feeds' : feeds
    }
    return render(request, 'dashboard/home.html', context)

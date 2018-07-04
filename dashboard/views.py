# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import feedparser

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import NoteForm
from datetime import date
# Create your views here.
def home(request):
    if request.method == "POST":
        # Add form data to database
        form = NoteForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['body']
            due_date = form.cleaned_data['due_date']

            Notes.objects.create(
                body = body,
                due_date = due_date
            ).save()
        return HttpResponseRedirect('/')
    else:
        form = NoteForm()
        note_list = Notes.objects.all()[:10]
        entries = feedparser.parse('https://www.novelupdates.com/rss.php?uid=101502&unq=59e2dfbf49d04&type=0&lid=local').entries[:10]
        context = {
            'notes' : note_list,
            'entries' : entries,
            'form' : form
        }
        return render(request, 'dashboard/home.html', context)

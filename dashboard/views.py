# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import feedparser

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import NoteForm
from datetime import date

# HOMEVIEW: Takes care of adding notes and viewing the home page
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
        # Create context and render the screen
        form = NoteForm()
        note_list = Notes.objects.all()[:10]
        entries = feedparser.parse('https://www.novelupdates.com/rss.php?uid=101502&unq=59e2dfbf49d04&type=0&lid=local').entries[:10]
        context = {
            'notes' : note_list,
            'entries' : entries,
            'form' : form
        }
        return render(request, 'dashboard/home.html', context)

# REMOVE_NOTE: Takes care of removing note then redirects back to the home page
def remove_note(request, pk):
    print('THIS DID RUN')
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        if request.method == 'POST':
            note.delete()
            return HttpResponseRedirect('/')

    form = NoteForm()
    note_list = Notes.objects.all()[:10]
    entries = feedparser.parse('https://www.novelupdates.com/rss.php?uid=101502&unq=59e2dfbf49d04&type=0&lid=local').entries[:10]
    context = {
        'notes' : note_list,
        'entries' : entries,
        'form' : form
    }
    return HttpResponseRedirect('/')

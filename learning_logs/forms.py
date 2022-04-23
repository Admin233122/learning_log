from cProfile import label
from dataclasses import field
from tkinter import Widget
from xml.dom.minidom import Entity
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': '  '}
        Widgets = {'text': forms.Textarea(attrs={'cols':80})}
        
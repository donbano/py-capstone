from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Word, Text
from .forms import WordForm, TextForm


def home(request):
    texts = Text.objects
    return render(request, 'home.html', {'texts': texts})


def text_view(request, pk):
    text = Text.objects.get(id=pk)
    return render(request, 'text_view.html', {'text': text})


def text_edit(request, pk):
    if request.method == "POST":
        form = TextForm(request.POST, request.FILES, instance=Text.objects.get(id=pk))
        if form.is_valid():
            text = form.save(commit=False)
            return redirect('/')
    else:
        form = TextForm(instance=Text.objects.get(id=pk))
    return render(request, 'text_edit.html', {'form': form})


def text_new(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.created_by = request.user
            # job.posted_by = User.objects.get(username="jSins")
            count(text)
            text.save()
            return redirect('/')
    else:
        form = TextForm()
    return render(request, 'text_edit.html', {'form': form})


def word_edit(request, pk):
    if request.method == "POST":
        form = WordForm(request.POST, request.FILES, instance=Word.objects.get(id=pk))
        if form.is_valid():
            word = form.save(commit=False)
            return redirect('/')
    else:
        form = WordForm(instance=Word.objects.get(id=pk))
    return render(request, 'word_edit.html', {'form': form})


def word_new(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.created_by = request.user
            # job.posted_by = User.objects.get(username="jSins")
            word.save()
            return redirect('/')
    else:
        form = WordForm()
    return render(request, 'word_edit.html', {'form': form})

def word_view(request):
    badwords = Word.objects.filter(isGood=False)
    goodwords = Word.objects.filter(isGood=True)
    return render(request, 'text_view.html', {'badwords': badwords, 'goodwords': goodwords})


def count(text):
    wordslist=Word.objects.all()
    goodwordslist = []
    badwordslist = []

    for word in wordslist:
        if word.isGood:
            goodwordslist.append(word.word)
        else:
            badwordslist.append(word.word)

    goodwordscount = 0
    badwordscount = 0

    wordlist = text.content.split()

    for word in wordlist:
        if word in goodwordslist:
            goodwordscount += 1
        if word in badwordslist:
            badwordscount += 1

    text.goodWordCount = goodwordscount
    text.badWordCount = badwordscount

    if goodwordscount >= badwordscount:
        text.isGood = True
    else:
        text.isGood = False

# Create your views here.

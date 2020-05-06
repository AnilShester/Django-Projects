from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'topicApp/index.html')


def topics(request):
    topics = Topic.objects.all()
    return render(request, 'topicApp/topics.html', {'topics': topics})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'topicApp/topic.html', {'topic': topic, 'entries': entries})

def new_topic(request):
    if request.method == "POST":
        forms = TopicForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('topics'))
    else:
        forms = TopicForm()
    return render(request, 'topicApp/new_topic.html', {'forms': forms})

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method == "POST":
        entry = EntryForm(data=request.POST)
        if entry.is_valid():
            new_entry = entry.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    else:
        entry = EntryForm()

    return render(request, 'topicApp/new_entry.html', {'topic': topic,
                                                       "entry": entry})


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id =entry_id)
    topic = entry.topic
    if request.method == "POST":
        form = EntryForm(instance= entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    else:
        form = EntryForm(instance=entry)
    return render(request, 'topicApp/edit_entry.html', {'form':form,
                                                        'entry': entry})
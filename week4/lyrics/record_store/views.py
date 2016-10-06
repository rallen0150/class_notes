from django.shortcuts import render

import datetime
from record_store.models import Song
# from django.http import HttpResponse

# Create your views here.
def index_view(request):
    context = {
        "my_name": "Robbie SON!!!",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }
    return render(request, "index.html", context)
    # return HttpResponse("I love web programming")

def lyrics_view(request, song_id):
    context = {
        "song": Song.objects.get(id=song_id)
    }
    return render(request, "lyrics.html", context)

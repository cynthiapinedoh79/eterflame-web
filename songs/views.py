from django.views.generic import ListView, DetailView
from .models import Song


class SongListView(ListView):
    model = Song
    template_name = 'songs/list.html'
    context_object_name = 'songs'

    def get_queryset(self):
        qs = Song.objects.filter(active=True)
        series = self.request.GET.get('series')
        if series:
            qs = qs.filter(series=series)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['series_choices'] = Song.SERIES_CHOICES
        ctx['active_series']  = self.request.GET.get('series', '')
        return ctx


class SongDetailView(DetailView):
    model = Song
    template_name = 'songs/detail.html'
    context_object_name = 'song'
    queryset = Song.objects.filter(active=True)

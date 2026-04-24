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

    def get_context_data(self, **kwargs):
        import re
        ctx = super().get_context_data(**kwargs)
        yt_embed = ''
        if self.object.youtube_url:
            match = re.search(
                r'(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})',
                self.object.youtube_url
            )
            if match:
                yt_embed = f'https://www.youtube.com/embed/{match.group(1)}?rel=0'
        ctx['yt_embed'] = yt_embed
        return ctx

from django.urls import path
from main.views import show_main, show_game, show_video

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('video/', show_video, name='show_video'),
    path('game/', show_game, name='show_game'),
]
from django.urls import path
from main.views import show_main, show_game, show_video, show_flappy, show_bulls_eye

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('video/', show_video, name='show_video'),
    path('game/', show_game, name='show_game'),
    path('game/flappy/', show_flappy, name='show_flappy'),
    path('game/bulls-eye/', show_bulls_eye, name='show_bulls_eye')
]
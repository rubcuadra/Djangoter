from django.conf.urls import include, url
from .views import BotView
urlpatterns = [url(r'^948d0261401ce4c2717ceba258cd1fa6adaacd4a3541c299c8/?$',BotView.as_view() )]

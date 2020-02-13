"""ChatServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from chat import views
from chat.views import HomePageView, ChatRoomView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('message/<str:id>/', ChatRoomView.as_view(), name='room'),
    # path('room/<int:room_id>/$', MessagesView.as_view(), name='messages'),
]

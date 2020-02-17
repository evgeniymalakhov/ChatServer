from django.urls import path, include
from chat import views
from chat.views import HomePageView, ChatRoomView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('message/<str:id>/', ChatRoomView.as_view(), name='room'),
    # path('room/<int:room_id>/$', MessagesView.as_view(), name='messages'),
]

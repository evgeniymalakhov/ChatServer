from django.shortcuts import render
from django.views.generic import TemplateView, View
from .mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


class ChatRoomView(LoginRequiredMixin, TemplateView):
    template_name = 'room.html'


# def room(request, room_name):
#     return render(request, 'room.html', {
#         'room_name': room_name
#     })

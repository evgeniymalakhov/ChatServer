from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, View
from .mixins import LoginRequiredMixin
from .models import Message, Room


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        context['users'] = User.objects.exclude(id=self.request.user.id)

        return context


class ChatRoomView(LoginRequiredMixin, TemplateView):
    template_name = 'messages.html'

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=Q(
            Q(room__first=kwargs['id']) | Q(room__second=kwargs['id']))
        )[:25]

        context['rooms'] = Room.objects.filter(
            Q(first__id=kwargs['id']) |
            Q(second__id=kwargs['id']))
        return context

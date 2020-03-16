from django.db.models import Q
from django.views.generic import TemplateView
from application.models import User
from .mixins import LoginRequiredMixin
from .models import Message, Room


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['users'] = User.objects.exclude(id=self.request.user.id)
        return context


class ChatRoomView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/messages.html'

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=
            Q(room__first=int(kwargs['id'])) & Q(room__second=int(self.request.user.id)) |
            Q(room__first=int(self.request.user.id)) & Q(room__second=int(kwargs['id'])))

        context['rooms'] = Room.objects.filter(
            Q(first__id=int(self.request.user.id)) | Q(second__id=int(self.request.user.id))
        )
        return context

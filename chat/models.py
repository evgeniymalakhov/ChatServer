from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models


class RoomManager(models.Manager):
    def get_or_new(self, user, other_user: int):
        user_id = user.pk
        if user_id == other_user:
            return None
        qlookup_1 = Q(first__pk=user_id) & Q(second__pk=other_user)
        qlookup_2 = Q(first__pk=other_user) & Q(second__pk=user_id)
        qs = self.get_queryset().filter(qlookup_1 | qlookup_2).distinct()

        if qs.count() == 1:
            return qs.first(), False
        elif qs.count > 1:
            return qs.order_by('').first(), False
        else:
            Klass = user.__class__
            user2 = Klass.object.get(pk=other_user)
            if user != user2:
                obj = self.model(
                    first=user,
                    second=user2
                )
                obj.save()
                return obj, True
            return None, False


class Room(models.Model):
    first = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first', default="")
    second = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second', default="")

    objects = RoomManager()

    @property
    def room_group_name(self):
        return f'room_{self.pk}'


class Message(models.Model):
    room = models.ForeignKey(
        Room,
        verbose_name=_("Room"),
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE)
    message = models.TextField(_("Message"))
    pub_date = models.DateTimeField(
        _("Date Created"),
        default=timezone.now)
    is_readed = models.BooleanField(
        _("Readed"),
        default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message


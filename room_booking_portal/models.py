from django.db import models
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError


@register_snippet
class RoomForBookingPortal(ClusterableModel, models.Model):
    title = models.CharField(max_length=264, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Room for the Booking Portal"
        verbose_name_plural = "Rooms for the Booking Portal"


class Booking(models.Model):
    user = models.ForeignKey("mechweb.CustomUser", null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=264, blank=False)
    reason = models.CharField(max_length=264, blank=True)
    room = models.ForeignKey(RoomForBookingPortal, on_delete=models.CASCADE)
    startTime = models.DateTimeField(blank=False)
    endTime = models.DateTimeField(blank=False)

    def clean(self):
        if self.startTime >= self.endTime:
            raise ValidationError("StartTime should be before endTime")
        return super().clean()

    def __str__(self):
        return self.title

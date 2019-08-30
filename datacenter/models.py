from django.db import models
from django.utils import timezone


def format_duration(duration):
  minutes = int(duration.total_seconds() // 60)
  return f"{minutes // 60}ч {minutes % 60}мин"


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
      if self.leaved_at:
        duration = self.leaved_at - self.entered_at
      else:
        duration = timezone.now() - self.entered_at
      return duration

    def is_long(self, minutes=60):
      return (self.get_duration().total_seconds() > minutes * 60)
     
    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

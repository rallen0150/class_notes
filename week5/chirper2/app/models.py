from django.db import models

# Create your models here.
class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')# for login

    def __str__(self):
        return self.body

    @property
    def score(self):
        return sum([chirp_obj.score for chirp_obj in self.vote_set.all()])

    class Meta:
        ordering = ("-created", )

class Vote(models.Model):
    user = models.ForeignKey('auth.User')
    chirp = models.ForeignKey('app.Chirp')
    value = models.BooleanField()

    class Meta:
        unique_together = ("user", "chirp")

    @property
    def score(self):
        if self.value:
            return 1
        return -1

    def __str__(self):
        return "{} - {}".format(self.chirp.body, self.score)

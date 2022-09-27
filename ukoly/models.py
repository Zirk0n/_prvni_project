from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.



class Ukol(models.Model):
    nazev = models.CharField(max_length=100)
    stav = models.BooleanField(default=False)
    #jmeno_autora = models.CharField(max_length=100)
    autor = models.ForeignKey(User,models.PROTECT,related_name="ukoly_autora", blank=True, null=True)

    def __str__(self):
        return self.nazev

    def get_absolute_url(self):
        return reverse("ukoly:detail_ukolu", kwargs={"index_ukolu": self.id})
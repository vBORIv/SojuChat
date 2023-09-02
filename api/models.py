from django.db import models


class VoteElement(models.Model):
    name = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)

class KeywordFreq(models.Model):
    keyword = models.CharField(max_length=100)
    freq = models.IntegerField()

    def __str__(self) -> str:
        return self.keyword
from django.db import models


class StoicQuote(models.Model):
    quote = models.TextField()
    philosopher = models.CharField(max_length=100)
    explanation = models.TextField()

    def __str__(self):
        return f'{self.philosopher}: "{self.quote}"'

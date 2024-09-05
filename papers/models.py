from django.db import models

class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField()
    year = models.PositiveIntegerField(null=True, blank=True)  
    citations = models.PositiveIntegerField()

    def __str__(self):
        return self.title

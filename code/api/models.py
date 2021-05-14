from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Book(models.Model):
    """Book model that holds an author and title.
    """
    author = models.CharField(_("Book author name"), max_length=64)
    title = models.CharField(_("Book title"), max_length=64)

    class Meta:
        unique_together = ['author', 'title']

    def __str___(self):
        return "{author}: {title}".format(author=self.author, title=self.title)

    
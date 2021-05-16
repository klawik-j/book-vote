from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from api.validators import validate_book

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

    def clean(self):
        return validate_book(self.author, self.title)

    def save(self, *args, **kwargs):
        new_author, new_title = self.clean()
        self.author = new_author
        self.title = new_title
        super(Book, self).save(*args, **kwargs)
    
    def average_rating(self):
        """
        Return average rating based on :models:`Review`.
        """
        return  self.reviews.all().aggregate(
                models.Avg('review'))['review__avg']

    @staticmethod
    def most_popular(n=5):
        books = Book.objects.annotate(review_number=models.Count('reviews'))
        books_sorted = books.order_by('-review_number')
        return books_sorted[:n]

    def number_of_reviews(self):
        """
        Return number of corresponding :models:`Review`.
        """
        return self.reviews.count()

class Review(models.Model):
    """Review model for :models:`api.Car`.
    Validates `review` to check if value is beween 0 and 5.
    """
    book = models.ForeignKey(Book,
                            on_delete=models.CASCADE,
                            related_name="reviews")
    review = models.IntegerField(_("Ratin from 0 to 5"),
                                validators=[
                                    MinValueValidator(0),
                                    MaxValueValidator(5)
                                ])
from typing import Tuple
import urllib.request
import json

from django.core.exceptions import ValidationError


def validate_book(author: str, title: str) -> Tuple[str, str]:
    """Validate if book exists via http://openlibrary.org/
    Ignores letter casing.
    Returns book author and title
    """
    url = "http://openlibrary.org/search.json?author={author}&title={title}".format(
        author=author, title=title
    ).replace(" ", "%20")
    book_data = urllib.request.urlopen(url).read()
    book_data = json.loads(book_data)

    if book_data.get("numFound") == 0:
        raise ValidationError(
            "Book {title} written by {author} has never benn published".format(
                author=author, title=title
            )
        )

    return (author, title)

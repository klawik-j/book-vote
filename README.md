#Book voting API
Api, handling voting on interesting books, utilizes DRF
##Requirements
Docker and docker-compose
#How to launch
1. Copy .env.template to .env and customize it to your liking
2. docker-compose up
3. You can acces the app on localhost:8080, database has been initialized and you are free to browse the API
##API
###Books
- `book/` **POST** `{author: -, title: -}` Creates a book, if the one have ever been publish  **GET** Returns a list of books with rating
- `book/<int:id>` **GET/DELETE** Returns or deletes particular book

###Reviews
- `review` **POST** `{book: -, review: -} Creates a review, that is linked to particular book

###TOP books
- 'popular' **GET** Returns top 5 most popular books based on number of reviews

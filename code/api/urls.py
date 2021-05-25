from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'book', viewset=views.BookViewSet, basename='book')
router.register(r'review', viewset=views.ReviewViewSet, basename='review')
router.register(r'popular', viewset=views.PopularBooksViewSet, basename='popular')

urlpatterns = [
    
] + router.urls

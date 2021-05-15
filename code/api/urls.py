from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'book', viewset=views.BookViewSet, basename='book')
router.register(r'review', viewset=views.Review, basename='review')

urlpatterns = [
] + router.urls
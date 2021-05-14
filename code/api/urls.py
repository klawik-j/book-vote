from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'book', viewset=views.BookViewSet, basename='book')

urlpatterns = [
] + router.urls
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('notes', NotesViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls

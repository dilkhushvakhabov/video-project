from rest_framework import routers
from .views import VideoViewSet

router = routers.SimpleRouter()

router.register('video', VideoViewSet)

urlpatterns = router.urls

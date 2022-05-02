from rest_framework import routers

from core import views

router = routers.SimpleRouter()
router.register(r"", views.ExecutionViewSet)
urlpatterns = router.urls

from rest_framework import routers
from bookstore.views import BookStoreViewSet

router = routers.DefaultRouter()
router.register('', BookStoreViewSet, basename = 'bookstore')

urlpatterns = router.urls
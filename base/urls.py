from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register,name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('groups/', GroupView.as_view({'get': 'list'}), name='groups'),
    path('users/', UserView.as_view({'get': 'list'}), name='groups'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('theme/', ThemeViewSet.as_view({'get': 'list', 'post': 'create'}), name='theme'),
    path('theme/<int:pk>/', ThemeViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='theme_detail'),
    path('package/', PackageViewSet.as_view({'get': 'list', 'post': 'create'}), name='package'),
    path('package/<int:pk>/', PackageViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='package_detail'),
    path('store_category/', StoreCategoryViewSet.as_view({'get': 'list','post':'create'}), name='store_category'),
    path('store_category/<int:pk>/', StoreCategoryViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='store_category_detail'),
    path('store/', StoreViewSet.as_view({'get': 'list','post':'create'}), name='store'),
    path('store/<int:pk>/', StoreViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='store_details'),
    path('payment/', PaymentViewSet.as_view({'get': 'list','post':'create'}), name='payment'),
    path('payment/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='payment_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

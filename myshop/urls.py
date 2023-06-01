from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path('coupon/', include('coupons.urls', namespace='couponst')),
    path("admin/", admin.site.urls),
    path('shop/', include('shops.urls', namespace='shops')),
    path('cart/', include('carts.urls', namespace='carts')),
    path('order/', include('orders.urls', namespace='orders')),
    path('payment/', include('payments.urls', namespace='payments')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

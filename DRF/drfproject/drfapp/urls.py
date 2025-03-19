from django.urls import path
from drfapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path("product/", product_view),
    path("order/", order_view),
    path("sortbyprice/", productSort),
    path("filterbystock/<int:value>/", productFilter),
    path("car/", carousal_view),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
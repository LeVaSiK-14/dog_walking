from rest_framework.routers import DefaultRouter as DR
from django.urls import path
from mainapp.views import(
    OrderListView, 
    OrderCreateView,
)


router = DR()



urlpatterns = [
    path(
        "orders/", 
        OrderListView.as_view(
            {
                'get': 'list'
            }
        ), 
        name="order-list"
    ),
    path(
        "orders/create/",
        OrderCreateView.as_view(
            {
                'post': 'create'
            }
        ), 
        name="order-create"
    ),
]

urlpatterns += router.urls

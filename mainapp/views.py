from rest_framework.response import Response
from rest_framework import status

from mainapp.models import(
    Order,
)

from mainapp.serializers import(
    OrderSerializer, 
    OrderCreateSerializer,
)

from rest_framework.viewsets import(
    GenericViewSet,
)
from rest_framework.mixins import(
    ListModelMixin,
    CreateModelMixin,
)

from rest_framework.permissions import(
    AllowAny,
)


class OrderListView(GenericViewSet, ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        AllowAny,
    )

    def list(self, request, *args, **kwargs):
        date = request.query_params.get('date', None)
        if not date:
            return Response(
                {
                    'error': "Please set query params 'date' in url"
                }
            )
        orders = Order.objects.filter(
            walk_date=date
        ).order_by(
            'walk_time'
        )
        serializer = OrderSerializer(orders, many=True)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )


class OrderCreateView(GenericViewSet, CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (
        AllowAny,
    )

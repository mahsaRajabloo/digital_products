from django.shortcuts import render

from django.utils import timezone
from django.utils.timezone import now


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import *

from .serializers import *
class PackageView(APIView):
    def get(self, request):
        packages = Package.objects.filter(is_enable=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscriptions = Subscription.objects.filter(
            user=request.user,
            # # just active subscriptions
            # expire_time__isnull=False,
            # expire_time__gt=current_time
        )


        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

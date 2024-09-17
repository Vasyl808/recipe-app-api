"""
Core views for app.
"""
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """Returns successful response."""

    def get(self, request):
        return Response(
            {'healthy': True}
        )

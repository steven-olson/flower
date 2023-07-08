from rest_framework.views import APIView
from rest_framework.response import Response


class PingView(APIView):
    """
    API to get or update or delete a single goal
    """

    def get(self, request):
        return Response({"msg": "pong"})

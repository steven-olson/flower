from flower_data.models import Goal
from flower_web.api.goal.goal_serializers import GoalDetailSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class GoalDetailView(APIView):
    """
    API to get or update or delete a single goal
    """

    @staticmethod
    def get_object(goal_id):
        try:
            return Goal.objects.get(id=goal_id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, _, goal_id):
        goal = self.get_object(goal_id)
        serializer = GoalDetailSerializer(goal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = GoalDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GoalListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    @staticmethod
    def get(_):
        snippets = Goal.objects.all()
        serializer = GoalDetailSerializer(snippets, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = GoalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

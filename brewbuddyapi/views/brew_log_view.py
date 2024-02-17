from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from ..models import Brew, BrewLog

class BrewLogView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for a single BrewLog
        Returns:
        Response -- JSON serialized BrewLog"""
        try:
            brew_log = BrewLog.objects.get(pk=pk)
            serializer = BrewLogSerializer(brew_log)
            return Response(serializer.data)
        except BrewLog.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for Multiple brewlogs for a single brew

        Returns:
          Response -- JSON serialized BrewsLogs"""
        brew = request.query_params.get('brew')
        brew_logs = BrewLog.objects.filter(brew=brew)
        serializer = BrewLogSerializer(brew_logs, many=True)
        return Response(serializer.data)

class BrewLogSerializer(serializers.ModelSerializer):
    """JSON serializer for BrewLog"""
    class Meta:
        model = BrewLog
        fields = ("id", "brew", "log", "date")
        depth = 1

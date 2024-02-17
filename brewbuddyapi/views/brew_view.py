from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from ..models import Brew, User

class BrewView(ViewSet):
    """brewbuddy api view set for brews"""

    def list(self, request):
        """Handle GET requests for Multiple Brews
        
        Returns:
          Response -- JSON serialized Brews"""
        brews = Brew.objects.all()
        serializer = BrewSerializer(brews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        
        Returns
          Respone -- JSON serialized brew instance"""

        user = User.objects.get(id=request.data["userId"])

        brew = Brew.objects.create(
          name = request.data["name"],
          description = request.data["description"],
          user = user,
        )

        serializer = BrewSerializer(brew)
        return Response(serializer.data)

class BrewSerializer(serializers.ModelSerializer):
    """JSON serializer for Brew"""
    class Meta:
        model = Brew
        fields = ("id", "name", "user", "description")
        depth = 1

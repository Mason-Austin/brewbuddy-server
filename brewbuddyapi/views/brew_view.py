from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from ..models import Brew, User, BrewCategory, Category

class BrewView(ViewSet):
    """brewbuddy api view set for brews"""

    @action(methods=['post'], detail=True)
    def add_category(self, request, pk):
        brew = Brew.objects.get(pk=pk)
        category = Category.objects.get(id=request.data['categoryId'])
        try:
            BrewCategory.objects.get(brew=brew, category=category)
            return Response({'message: This brew already has this category'})
        except BrewCategory.DoesNotExist:
            BrewCategory.objects.create(
              brew=brew,
              category=category
            )
            serializer = BrewSerializer(brew)
            return Response(serializer.data)
          
    @action(methods=['delete'], detail=True)
    def remove_category(self, request, pk):
        brew = Brew.objects.get(pk=pk)
        category = Category.objects.get(id=request.data['categoryId'])
        brew_category = BrewCategory.objects.get(brew=brew, category=category)
        brew_category.delete()
        serializer = BrewSerializer(brew)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for a single Brew
        Returns:
          Response -- JSON serialized brew"""
        try:
            brew = Brew.objects.get(pk=pk)
            serializer = BrewSerializer(brew)
            return Response(serializer.data)
        except Brew.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for Multiple Brews
        
        Returns:
          Response -- JSON serialized Brews"""
        brews = Brew.objects.all()
        serializer = BrewSerializer(brews, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle POST operations
        
        Returns:
          Response -- JSON serialized brew instance"""
        brew = Brew.objects.get(pk=pk)
        brew.name=request.data["name"]
        brew.description=request.data["description"]
        brew.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations
        
        Returns
          Response -- JSON serialized brew instance"""

        user = User.objects.get(id=request.data["userId"])
        categories = request.data["categories"]

        brew = Brew.objects.create(
          name = request.data["name"],
          description = request.data["description"],
          user = user,
        )

        for s_category in categories:
            category = Category.objects.get(id=s_category)
            BrewCategory.objects.create(
              brew = brew,
              category = category
            )

        serializer = BrewSerializer(brew)
        return Response(serializer.data)

    def destroy(self, request, pk):
        brew = Brew.objects.get(pk=pk)
        brew.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BrewSerializer(serializers.ModelSerializer):
    """JSON serializer for Brew"""
    class Meta:
        model = Brew
        fields = ("id", "name", "user", "description", "categories")
        depth = 1

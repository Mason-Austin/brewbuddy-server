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
        """This function creates the relation table between one brew and one category"""

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
        """This function deletes the relation table between one brew and one category"""

        brew_category = BrewCategory.objects.get(pk=pk)
        brew_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

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
        categories = request.data["categories"]
        brew_categories = BrewCategory.objects.filter(brew=brew)
        def selected_categories(brew_categories):
            return [brew_category.category.id for brew_category in brew_categories]

        brew.name=request.data["name"]
        brew.description=request.data["description"]
        brew.image=request.data["image"]
        brew.stage=request.data["stage"]
        brew.save()
        
        for s_category in categories:
            if s_category not in selected_categories(brew_categories) :
              category = Category.objects.get(id=s_category)
              BrewCategory.objects.create(
                brew = brew,
                category = category
              )

        for category_id in selected_categories(brew_categories):
            if category_id not in categories :
              category  = Category.objects.get(id=category_id)
              brew_category = BrewCategory.objects.get(brew=brew, category=category)
              brew_category.delete()
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
          image = request.data["image"],
          stage = request.data["stage"],
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
      
class BrewCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for BrewCategory"""
    id = serializers.ReadOnlyField(source='category.id')
    label = serializers.ReadOnlyField(source='category.label')

    class Meta:
      model = BrewCategory
      fields = ('id', 'label')
class BrewSerializer(serializers.ModelSerializer):
    """JSON serializer for Brew"""
    categories = BrewCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Brew
        fields = ("id", "name", "user", "description", "image", "stage", "categories")
        depth = 1

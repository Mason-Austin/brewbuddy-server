from rest_framework.decorators import api_view
from rest_framework.response import Response
from brewbuddyapi.models import User

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the levelupapi_user table
    user = User.objects.create(
        name=request.data['name'],
        uid=request.data['uid'],
        bio=request.data['bio']
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'uid': user.uid,
        'name': user.name,
        'bio': user.bio,
        'created': user.created
    }
    return Response(data)

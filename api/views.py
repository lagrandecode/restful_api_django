from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['GET'])
def getdata(request):
    context = {
        'name' : 'oluwaseun','age': 22
    }
    return Response(context)
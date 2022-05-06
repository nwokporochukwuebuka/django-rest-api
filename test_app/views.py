#from django.shortcuts import render
#from rest_framework.views import APIView
#from django.http import JsonResponse, response
# We remove this and use the simple serializer
#from django.forms.models import model_to_dict
'''from .serializers import SimpleSerializer
from rest_framework import generics
from test_app.models import TestModel'''
from rest_framework import viewsets

# Create your views here.
#def simple(request):
    # perform operations
    #a = 30 + 50
    #return response.HttpResponse(f"<h1>{a}</h1>")
    # if we want to return a json response
    #return JsonResponse({'ans': a})
    #To access method type we are using 
    #return JsonResponse({'data': request.method.lower()})
    #method = request.method.lower()
    #if method == 'get':
        #return JsonResponse({'data': [1,2,3,4]})
    #elif method == 'post':
        #return JsonResponse({"data": "Added data successfully!"})
    #elif method == 'put':
        #return JsonResponse({"data": "Updated data successfully!"})

    #return JsonResponse({"error": 'method not allowed'})

'''class Simple(APIView):

    def post(self, request):
        To use as a validator
        serializer = SimpleSerializer(data=request.data)

        # made sure all the fields are supplied
        serializer.is_valid(raise_exception=True)

        new_test_content = TestModel.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            phone_number=request.data['phone_number'],
            is_alive=request.data['is_alive'],
            amount=request.data['amount']
        )

        serializer.save()
        
        #print(new_test_content)
        return JsonResponse({'data': request.data})

    def get(self, request):
        content = TestModel.objects.all()
        return JsonResponse({'data': SimpleSerializer(content, many=True).data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)

        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})

        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Objects does not exist"})

        # Returnin for only that id/instance
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})'''

'''class SimpleGenerics(generics.ListCreateAPIView):
    Allows for only POST and GET request
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer'''

'''class SimpleGenericUpdate(generics.UpdateAPIView):
    Allows for PUT and PATCH method. other than the other method which just allows fo get and post and that's why 
    there is a lookup field called id. We can also make it pk
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"
    '''


'''class SimpleViewset(viewsets.ModelViewSet):
    Allows us to create our own router that does allow create and update 
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    '''
 


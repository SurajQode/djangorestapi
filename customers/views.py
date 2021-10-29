# from django.db.models import query
# from django.shortcuts import render
# from rest_framework import serializers
from .models import Customer
from .serializers import CustomerSerializer
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from django.http import Http404
from rest_framework import mixins, generics

# Create your views here.



class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




# class CustomerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView ):

#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
        


# class CustomerDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def get(self, request, pk):
#         return self.retrieve(request)

#     def put(self, request, pk):
#         return self.update(request)

#     def delete(self, request, pk):
#         return self.destroy(request)



# class CustomerList(APIView):
    # def get(self, request):
    #     customer = Customer.objects.all()
    #     serializers = CustomerSerializer(customer, many=True)
    #     return Response(serializers.data)

    # def post(self, request):
    #     serializers = CustomerSerializer(data= request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





# class CustomerDetails(APIView):
#     def get_customer(self, pk):
#         try:
#             return Customer.objects.get(pk=pk)
#         except Customer.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         customer = self.get_customer(pk)
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         customer = self.get_customer(pk)
#         serializer = CustomerSerializer(customer, data= request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         customer = self.get_customer(pk)
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # @csrf_exempt
# @api_view(['GET', 'POST'])
# def customers_list(request):
#     if request.method == 'GET':
#         customer = Customer.objects.all()
#         serializers = CustomerSerializer(customer, many=True)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         # data = JSONParser().parse(request)
#         # serializers = CustomerSerializer(data=data)
#         serializers = CustomerSerializer(data= request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_details(request, pk):
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         # serializer = CustomerSerializer(customer, data=data)
#         serializer = CustomerSerializer(customer, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


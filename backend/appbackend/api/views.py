from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FormSerializer
import json
from .models import FormModel

# Create your views here.

## add form data api
class AddFormData(APIView):
    def post(self,request):
        data_list=request.data
        added_data=[]
        if data_list:
            for data in data_list:
                print(type(data))

                serializer=FormSerializer(data=data)
                if serializer.is_valid():
                    obj=serializer.save()
                    added_data.append(obj)
                else:
                    for obj in added_data:
                        obj.delete()
                    return Response({'message':'please enter valid data','error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

                print(data)
            return Response({'message':'data added successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'please enter data'},status=status.HTTP_400_BAD_REQUEST)
        

## get form data api
class GetFormData(APIView):
    def get(self,request):
        form_data=FormModel.objects.all()
        serializer=FormSerializer(form_data,many=True)
        if form_data.exists(): 
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'No data found'},status=status.HTTP_404_NOT_FOUND)
        

## get form data api
class DeleteData(APIView):
    def post(self,request):
        uid=request.data.get('uuid')
        print(uid)
        form_data=FormModel.objects.filter(uuid=uid)
        if form_data:
            form_data.delete()
            return Response({'message':'Row deleted'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'clicked data not found please refresh the page and try again'},status=status.HTTP_404_NOT_FOUND)
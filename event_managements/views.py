from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import EventUserCreationForm

from .serializers import EventSerializer, TroupeSerializer
from .models import Event, Troupe
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SignUpView(CreateView):
    form_class = EventUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class EventAPIView(APIView):

    def get(self, request):
        if request.user.is_client==True:
            events = Event.objects.filter(client=request.user)
        elif request.user.is_clown==True:
            events = Event.objects.filter(troupe__clown=request.user)
        else:
            events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_client==True:
            return Response("Not Allowed to create Events")
        elif request.user.is_clown==True:
            return Response("Not Allowed to create Events")
        elif request.user.is_troupe_leader==True:
            serializer = EventSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetails(APIView):
    def get_object(self, id):
        try:
            return Event.objects.get(id=id)
        except Event.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        event=self.get_object(id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self,request, id):
        if request.user.is_client==True and Event.client==request.user:
            event = self.get_object(id)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.user.is_clown==True and Event.troupe__clown==request.user:
            event = self.get_object(id)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You are not allowed to make any changes")



    def delete(self, request, id):
        if request.user.is_client == True or request.user.is_clown == True or request.user.is_troupe_leader == True:
            return Response("Events are not meant to be deleted")
        else:
            event = self.get_object(id)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class TroupeAPIView(APIView):

    def get(self, request):
        if request.user.is_troupe_leader == True:
            troupes = Troupe.objects.filter(leader=request.user)
            serializer = TroupeSerializer(troupes, many=True)
            return Response(serializer.data)
        else:
            return Response("Unauthorised to View Troupe Details")




    def post(self, request):
        if request.user.is_troupe_leader == True:
            serializer = TroupeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unauthorised to Create New Troupes")



class TroupeDetails(APIView):
    def get_object(self, id):
        try:
            return Troupe.objects.get(id=id)
        except Troupe.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        troupe=self.get_object(id)
        serializer = TroupeSerializer(troupe)
        return Response(serializer.data)

    def put(self,request, id):

        troupe = self.get_object(id)
        if request.user.is_troupe_leader and troupe.leader == request.user:
            serializer = TroupeSerializer(troupe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You cannot update this troupe info")


    def delete(self, request, id):
        if request.user.is_client == True or request.user.is_clown == True or request.user.is_troupe_leader == True:
            return Response("Events are not meant to be deleted")
        else:
            troupe = self.get_object(id)
            troupe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

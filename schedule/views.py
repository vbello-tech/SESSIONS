from django.shortcuts import render, get_object_or_404
from rest_framework import exceptions, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import *
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import *
from rest_framework.permissions import *
from business.models import Business
from django.core.exceptions import ObjectDoesNotExist
import random, string
from django.utils import timezone


# Create your views here.

#generate random 5 digits that would be used as business code.
def code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

@api_view(['POST'])
def registration(request):
    if request.method == "POST":
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Sucessfully created an account"
            data['username'] = user.username
            data['token'] = Token.objects.get(user=user).key
        else:
            data = serializer.errors
        return Response(data)

# FUNCTION TO BOOK A SESSION WITH A BUSINESS
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def booksession(request, pk):
    # business logged in user would book a session with
    business = get_object_or_404(Business, pk=pk, active=True)
    # check if user has an opened session with business
    session, created = BookedSession.objects.filter(
        user=request.user,
        opened = True,
    )
    if session.exists():
        #msg when user has an open session
        return Response({
            'message': f'you have an open session with {business.name}'
        })
    else:
        # CREATE AN open session
        session, created = BookedSession.objects.get_or_create(
            user=request.user,
            admin=business.admin,
            opened=True,
            ref_code=code(),
            business=business,
        )
        return Response ({
            'message': f'you have opened a session with {business.name}',
            'session code': session.ref_code
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def accept_session(request, pk):
    logged_in_user = request.user
    bookedsession = get_object_or_404(
        BookedSession,
        pk=pk,
        opened=True
    )
    if logged_in_user == bookedsession.business.admin:
        bookedsession.active=True
        return Response({
            'message': f'Session is active. Remember to close section after you complete the session.',
            'session code': bookedsession.ref_code
        })
    else:
        return Response({
            'message': f'You are not the admin of {bookedsession.business.name}',
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def decline_session(request, pk):
    logged_in_user = request.user
    bookedsession = get_object_or_404(
        BookedSession,
        pk=pk,
        opened=True
    )
    if logged_in_user == bookedsession.business.admin:
        bookedsession.active = False
        bookedsession.opened = False
        bookedsession.admin_closed = True
        return Response({
            'message': f'Session is has been closed',
            'session code': bookedsession.ref_code
        })
    else:
        return Response({
            'message': f'You are not the admin of {bookedsession.business.name}',
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def userclosesession(request, pk):
    # check if user has an opened session with business
    session, created = BookedSession.objects.get(
        pk=pk,
        user=request.user,
        active=True,
    )
    if session.exists():
        session.user_colsed=True,
        session.active=False,
        session.opened=False
        session.user_close_func()
        return Response({
            'message': f'session closed sucessfully',
            'session code': session.ref_code
        })
    else:
        if not session.exists():
            return Response ({
                'message': f"you don't have an open session with {session.business.name}",
            })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def adminclosesession(request, pk):
    # check if user has an opened session with business
    session, created = BookedSession.objects.get(
        pk=pk,
        admin=request.user,
        active=True
    )
    if session.exists():
        session.admin_colsed = True,
        session.active = False,
        session.opened = False
        session.admin_close_func()
        return Response({
            'message': f'session closed sucessfully',
            'session code': session.ref_code
        })
    else:
        if not session.exists():
            return Response ({
                'message': f'no open sessions with {session.user.username}',
            })

class UserBookedSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = BookedSession.objects.filter(user=request.user, active=True)
        serializer = BookedSessionSerializer(order, many=True)
        return Response(serializer.data)

class AdminOpenedSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = BookedSession.objects.filter(admin=request.user, active=True)
        serializer = BookedSessionSerializer(order, many=True)
        return Response(serializer.data)


class UserClosedSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = BookedSession.objects.filter(user=request.user, closed=True)
        serializer = BookedSessionSerializer(order, many=True)
        return Response(serializer.data)


class AdminClosedSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = BookedSession.objects.filter(admin=request.user, closed=True)
        serializer = BookedSessionSerializer(order, many=True)
        return Response(serializer.data)


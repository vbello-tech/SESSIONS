from django.urls import path
from .views import *

urlpatterns = [
    path('book/<int:pk>/', booksession, name="booksession"),
    path('accept/<int:pk>/', booksession, name="acceptsession"),
    path('decline/<int:pk>/', booksession, name="declinesession"),
    path('user-close/<int:pk>/', booksession, name="user_close_session"),
    path('admin-close/<int:pk>/', booksession, name="admin_close_session"),
    path('user-booked/', UserBookedSessionView.as_view(), name="user_booked"),
    path('user-closed/', UserClosedSessionView.as_view(), name="user_closed"),
    path('admin-closed/', AdminClosedSessionView.as_view(), name="admin_closed"),
    path('admin-opened/', AdminOpenedSessionView.as_view(), name="admin_opened"),
]
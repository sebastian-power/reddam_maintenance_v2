from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    """Get current authenticated user's information.

    Args:
        request (_type_): Request object containing user information.

    Returns:
        Response: Returns user information or an error message.
    """
    user = request.user
    return Response(
        {
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active,
            "date_joined": user.date_joined,
        }
    )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_account(request):
    """Delete current user account"""
    user = request.user
    user.delete()
    return Response(
        {"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


def test_view(request):
    """
    A simple test view to check if the user is authenticated.
    """
    if request.user.is_authenticated:
        return render(request, "test.html", {"user": request.user})
    else:
        return render(request, "test.html", {"user": None})

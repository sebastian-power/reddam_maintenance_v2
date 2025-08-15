from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom registration serializer that only requires email and password
    """

    username = None  # Remove username field

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # Only return email and password data
        return {
            "email": data.get("email"),
            "password1": data.get("password1"),
        }

    def save(self, request):
        user = super().save(request)
        return user

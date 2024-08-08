from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
import pandas as pd
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from kilimo_guard.common_functions import CommonFunctions
from kilimo_guard.error_handler import ErrorHandler
from kilimo_guard.models import Users
from kilimo_guard.multithreading import Multithreading
from kilimo_guard.prediction_model import PredictionModel
from kilimo_guard.serializers import UsersSerializer
from kilimo_project import settings


# Create your API views here.
@api_view(['POST'])
@permission_classes([])
def train_model(request):
    try:
        Multithreading.start_model_training()
        return Response("Successfully started to train the model.", status=status.HTTP_200_OK)
    except Exception as error:
        ErrorHandler.django_handle_error(error)
        return Response("An error occured while starting to train the model", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def predict(request):
    try:
        # Get user input from the form            
        crop_type = request.data.get("crop_type")
        date = pd.to_datetime(request.data.get("date"))
        # location

        # Get this through API
        temperature = float(request.data.get("temperature"))
        rainfall = float(request.data.get("rainfall"))
        humidity = float(request.data.get("humidity"))
        wind_speed = float(request.data.get("wind_speed"))
        soil_moisture = float(request.data.get("soil_moisture"))

        # Create a DataFrame from user input
        user_input = {
            'date': [date],
            'temperature': [temperature],
            'humidity': [humidity],
            'rainfall': [rainfall],
            'wind_speed': [wind_speed],
            'crop_type': [crop_type],
            'soil_moisture': [soil_moisture],
        }

        results = PredictionModel.make_prediction(user_input=user_input)

        return Response(results, status=status.HTTP_200_OK)
    except Exception as error:
        ErrorHandler.django_handle_error(error)
        return Response("An error occured while making a prediction", status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        try:
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            ErrorHandler.django_handle_error(error)
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password").strip()
            user = Users.objects.get(username=username)
            print(f"User Found: {user.username}, Hashed password: {user.password}")
            if user.check_password(password):
                access_token = CommonFunctions.generate_jwt_token(user)
                serializer = UsersSerializer(user, many=False)
                return Response({'message': "User Logged In Successfully!", 'access_token': str(access_token),
                                 'user': serializer.data},
                                status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            ErrorHandler.django_handle_error(error)
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        try:
            token = request.data.get("token")
            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as error:
            ErrorHandler.django_handle_error(error)
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)

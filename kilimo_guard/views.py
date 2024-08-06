from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
import pandas as pd
from kilimo_guard.error_handler import ErrorHandler
from kilimo_guard.multithreading import Multithreading
from kilimo_guard.prediction_model import PredictionModel

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
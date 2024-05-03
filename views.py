from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .consumers import recognize
# import numpy as np
from keras.models import load_model
# import os
# import glob
# import cv2
# from .consumers import recognize_gesture as recognize_gesture_function
recognize_flag = False
# import subprocess
model = load_model('cnn_model_keras2.keras')

@csrf_exempt
def index(request):
    """
    Renders the index page.
    """
    return render(request, './frontends/templates/index.html')

def recognize_gesture_button(request):
    global recognize_flag
    if request.method == 'POST':
        # Run the recognize() function here
        recognize_flag = True
        print("recognize_flag set to:", recognize_flag)
        recognize()
        # Return a JSON response with the result
        return JsonResponse({'message': 'Recognition successful'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

recognize_gesture_button = csrf_exempt(recognize_gesture_button)

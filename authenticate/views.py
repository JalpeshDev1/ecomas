import json
import threading
import logging
from django.shortcuts import render
from utility.authenticate import AuthenticateUtility

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from utility.jwt_token import JWTAuthentication
from .models import *

logger = logging.getLogger(__name__)

jwt_obj = JWTAuthentication()
authenticate_obj = AuthenticateUtility()


class Register(APIView):
    def post(self, request):
        
        logger.info("Register : Execution start ")
        try:
            data = request.data
            logger.debug(f"data  : {data}")
            # Extract user registration data from the provided dictionary
            first_name = data["first_name"]
            last_name = data['last_name']
            username = data["username"]
            email = data["email"]
            password = data["password"]
            
            val = authenticate_obj.register(first_name,last_name, username, email, password)
            # email_thread = threading.Thread(target=email_obj.registration_complete_mail,args=(first_name,email),)
            # email_thread.start()
            
            logger.info("RegisterStudent : Execution End ")
            return Response(
                {
                    "status_code": 200,
                    "response_msg": "Register Successfully",
                    "data": {},
                },
                status=status.HTTP_201_CREATED,
            )
        except KeyError :
            return Response( { "status_code": 400,"response_msg": "some parameters are missing","data": {},}, status=400)
        except Exception as e:
            logger.error("Error during user registration")
            return Response( { "status_code": e.status_code,"response_msg": e.message,"data": {},}, status=e.status_code,)


class Login(APIView):
    def post(self, request):
        
        logger.info("Login : Execution start")
        try:
            data = request.data
            logger.debug(f"data  : {data}")
            # Extract email and password from the input data
            password = data["password"]
            username = data["username"]
            
            val = authenticate_obj.login(password, username)
            logger.debug(f" user : {val}")
            
            user = User.objects.filter(username=username).first()
            jwt_token = jwt_obj.create_jwt(username)
            logger.debug(f'jwt_token : {jwt_token}')
            
            user.jwt = jwt_token
            user.save()
            logger.info("Login : Execution End")
            return Response(
                {
                    "status_code": 200,
                    "response_mesg": "Login successful",
                    "data": {"token": jwt_token,
                                "user_id": user.id},
                },
                status=status.HTTP_200_OK,
            )
        except KeyError :
            return Response( { "status_code": 400,"response_msg": "some parameters are missing","data": {},}, status=400)
        except Exception as e:
            logger.error("Error during login")
            return Response( { "status_code": e.status_code,"response_msg": e.message,"data": {},}, status=e.status_code,)

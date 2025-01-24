import logging
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from authenticate.models import *
from exceptions.authenticate_exception import *
from exceptions.common_exception import *
from datetime import date
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

class AuthenticateUtility:

    def register(self,first_name:str,last_name:str, username:str, email:str, password:str) -> int:
        
        logger.info("Execution Start")
        try:
            # Check if a user with the same email or username already exists
            if User.objects.filter(email=email).exists():
                raise EmailAlreadyExists(400)  # User already exists
            
            # Create a new user in the database
            user = User.objects.create(
                first_name=first_name,
                last_name = last_name,
                username=username,
                email=email,
                password=make_password(password),
                verify=False,
            )
            logger.info("Execution End")
            return 0
        except Exception as e:
            logger.error(e)
            raise SystemException(500,str(e))


    def login(self,password: str, username: str) -> int:
        
        logger.info("Execution Start")
        try:
            
            user = User.objects.get(username=username)
            # Retrieve the user object based on the provided email
            logger.debug(f"original password : {password} , hashed password : {user.password}")
            # Check if the provided password matches the hashed password in the database
            if check_password(password, user.password):
                logger.info("Execution End")
                return 0
            else:
                raise WrongPassword(400)
            
        except ObjectDoesNotExist:
            raise EmailNotRegistered(404)
        except Exception as e:
            logger.error(e)
            raise SystemException(500,str(e))
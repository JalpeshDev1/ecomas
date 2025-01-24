import logging
import jwt
from ecomas.settings import SECRET_KEY
from rest_framework.exceptions import AuthenticationFailed, ParseError
from datetime import datetime, timedelta
from authenticate.models import User

logger = logging.getLogger(__name__)


class JWTAuthentication:
    """
    This class is used to handle all functionalities of JWT token like token generation, token authentication,
    getting token from header
    """

    @classmethod
    def create_jwt(cls, username: str) -> str:
        """
        This method is use to generate jwt token for user authentication using username
        Params:
            username(string) : unique name of user
        Returns:
            jwt_token(string) : encoded string of user data
        """
        logger.info("Execution Start")
        try:
            # getting user data using username from database
            user = User.objects.filter(username=username).first()
            # making payload to generate jwt token
            logger.debug(f"user id : {user.id}")
            payload = {
                "user_id": user.id,
                "exp": datetime.utcnow() + timedelta(days= 5),
                # int(
                #     (datetime.now() + JWT_CONF["ACCESS_TOKEN_LIFETIME"]).timestamp()
                # ),
                "iat": datetime.utcnow().timestamp(),
                "username": user.email,
            }
            logger.debug(f"payload : {payload}")
            # encoding payload using secret key and HS256 algorithm to make jwt token
            jwt_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            logger.info("Execution End")
            return jwt_token
        except Exception as e:
            logger.error(f"Error : {e}")
            return e

    @classmethod
    def get_token_from_header(cls, token: str) -> str:
        """
        This method is use to remove 'Bearer word from jwt token'
        Params:
            token(string) : jwt token
        Returns:
            token(string) : jwt token without Bearer word and extra spaces
        """
        logger.info("Execution Start")
        try:
            # jwt token comes in header with Bearer word attached in starting, removing it and getting actual jwt token
            token = token.replace("Bearer", "").replace(" ", "")
            logger.info("Execution End")
            return token
        except Exception as e:
            logger.error(f"Error : {e}")
            return e

    def authenticate(self, request):
        """
        This method is use to authenticate jwt token and returns user object and payload provided while generating jwt token
        Params:
            request(object) : request object that contains Authorization in headers
        Returns:
            user(object) : user object
            payload(dictionary) : data dictionary that is provided while generating jwt token
        """
        logger.info("Execution Start")
        # getting jwt token from request headers
        jwt_token = request.headers["Authorization"]
        # if jwt token is not available returning None
        if jwt_token is None:
            return None

        # getting actual jwt token after removing Bearer word
        jwt_token = JWTAuthentication.get_token_from_header(jwt_token)

        # decoding token and verifyig its signature
        try:
            # decoding token and getting user object and its payload
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            # in case token gets invalide raising Invalide Signature Exception
            raise AuthenticationFailed("Invalid Signature")
        except:
            # raising Parsing error in case Something is wrong
            raise ParseError()

        # getting username from payload
        username = payload.get("username")
        # in case username not found in payload raising Authentication Failed
        if username is None:
            raise AuthenticationFailed("No such user found in JWT!")

        # getting user data from database
        user = User.objects.filter(username=username).first()
        # if user is not available in database raising user not found
        if user is None:
            raise AuthenticationFailed("User Not Found")
        logger.info("Execution End")
        return user, payload
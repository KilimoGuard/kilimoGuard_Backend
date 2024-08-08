import jwt
from rest_framework.exceptions import ValidationError
from kilimo_project import settings


class CommonFunctions:
    def generate_jwt_token(user):
        payload = {
            'user_id': str(user.id),
            'username': user.username,
            'email': user.email,
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

    def decode_jwt_token(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValidationError('Token is expired')
        except jwt.InvalidTokenError:
            raise ValidationError('Token is invalid')
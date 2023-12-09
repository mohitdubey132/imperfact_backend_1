# token_utils.py
from rest_framework_simplejwt.tokens import AccessToken

def get_user_id_from_token(request):
    authorization_header = request.headers.get('Authorization', '')
    
    try:
        # Extract the token from the Authorization header
        token = authorization_header.split(' ')[0]
        # print(token)
        # Decode the token to get the payload
        decoded_token = AccessToken(token).payload
        # print(decoded_token)
        # Retrieve the user ID from the payload
        user_id = decoded_token.get('user_id')
        
        return user_id
    except Exception as e:
        # Handle invalid token or other exceptions
        print(f"Error: {e}")
        return None

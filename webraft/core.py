import datetime
from cryptography.fernet import Fernet
from .ipinfo import IPInfo
from user_agents import parse
import jwt
try:
    from django.middleware import csrf
    from django_user_agents.utils import get_user_agent
except:
    pass
# New Files
from .validate import validateAlgorithm as va
from .validate import validateExpirytoken as ve
from .validate import validateFramework as vf
from . import engine
from .modify import Modification


class JWTToken:
    def __init__(self, secret_key=None,expiry_token=None,framework=None,algorithm=None):
        """
        The JWTToken class that creates and reads JSON Web Tokens
        with a specified secret key, expiry date, and framework.
        
        """
        ve(expiry_token)
        vf(framework)
        va(algorithm)
        self.secret_key = secret_key
        self.expiry_token = int(expiry_token)
        self.framework=framework
        self.today = datetime.datetime.now()
        self.algorithm = algorithm
        
        
    def create(self,request,data:list) -> str:
        
        self.data = data
        self.request = request
        self.data =  Modification.modify(self.data,self.request,self.expiry_token,self.framework)
        return engine.create(data,self.secret_key,self.algorithm)
        # return engine.create(self.request)
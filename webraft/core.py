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
from .process import ProcessToken


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
        self.data =  ProcessToken.modify(
            data=data,
            request=request,
            expiry_token=self.expiry_token,
            )
        return engine.create(
            data=self.data,
            secret_key=self.secret_key,
            algorithm=self.algorithm
            )

    def read(self, request, args:list,header=None) -> list or dict:
        
        self.request = request
        self.args = args
        self.header = header
        if header == None:
            self.header = 'authorization'

        # if self.is_authenticated() == False:
        #     return {"invaild-token": "token expire"}
        try:
            return ProcessToken.getHeader(self,
                request=request,
                framework=self.framework,
                header=self.header,
                algorithm=self.algorithm,
                secret_key = self.secret_key,
                args=args
            )
        except KeyError as e:
            raise KeyError(f"invalid key {e}")
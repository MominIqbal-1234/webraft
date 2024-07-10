import datetime
from cryptography.fernet import Fernet
from .ipinfo import UserIPData,publicip
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
from .validate import check_token_expiry as cte


from . import engine
from .process import ProcessToken
from .generator import GenerateKey





__name__ = "webraft"
__verion__ = "0.5"

"""


This project developed by Momin Iqbal
Support : mefiz.com
================================================================================================================

WebRaft Support Four Python web-framework 
1) Django
2) Flask
3) FastAPI
4) Bottle

Feuture:
The code defines several classes for creating and reading JSON Web Tokens, extracting user agent
information, retrieving IP data, and creating and reading API keys.
----------------------------------------------------------------------------------------------------------------

Check Our Site : https://mefiz.com

"""




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
        """
        This function creates a token using the provided data and request.
        
        :param request: The request object
        :param data: The `data` parameter is a variable
        """
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

    def read(self, request, args:list=None,header=None) -> list or dict:
        """
        This read function using the provided data and request.
        
        :param request: The HTTP request object
        :param header: The header parameter is an optional argument that specifies the name of the
        header that contains the authentication token. If this parameter is not provided, the default
        header name 'authorization' will be used
        :return: a list or a dictionary.
        """
        self.request = request
        self.args = args
        self.header = header
        if header == None:
            self.header = 'authorization'

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

    def checkExpiry(self, token:str):
        """
        return : bool
        """
        expiryTime = (engine.read({
            "token":token,
            "secret_key":self.secret_key,
            "algorithm":self.algorithm
        })['expiry_time'])
        return cte(expiryTime)

    def getToken(self,request,header):
        """
        get token in request header
        return : bool
        """
        if self.framework == 'fastapi' or 'flask' or 'bottle':
            return (request.headers[header])

        elif self.framework == 'django':  
            return (request.headers[header])



    

def generator():
    """
    Generate Random keys
    """
    
    return GenerateKey.generate_key()




def PublicIP():
    """
    Get Piblic IP
    """
    return publicip()

def userIpinfo(request):
    """
    Get IP Data
    """
    return UserIPData(request)



class MetaData:
    def __init__(self,request,framework=None):
        
        """
        The MetaData class extracts user agent information from a request and
        provides methods to retrieve device, OS, browser, and other related information.
        """
        if framework == 'fastapi' or framework =='flask' or framework =='bottle':
            self.user_agent_string = request.headers.get('User-Agent')
            self.user_agent = parse(self.user_agent_string)
        else:
            self.user_agent = get_user_agent(request)
  

        self.device_is = self.user_agent.device.family
        self.os_is = self.user_agent.os.family
        self.browser_is = self.user_agent.browser.family
        self.deviceIs = self.user_agent.get_device()
        self.osIs = self.user_agent.get_os()
        self.browserIs = self.user_agent.get_browser()
        self.mobileIs = self.user_agent.is_mobile
        self.tabletIs = self.user_agent.is_tablet
        self.touchCapableIs = self.user_agent.is_touch_capable
        self.pcIs = self.user_agent.is_pc
        self.botIs = self.user_agent.is_bot
        self.emailClientIs = self.user_agent.is_email_client



class APIKey:
    """
    The APIKey class provides for creating, reading, retrieving data from API keys.
    """
    def __init__(self, api_secret_key=None,expiry_token=None,algorithm=None):
        self.api_secret_key = api_secret_key
        self.algorithm = algorithm
        self.expiry_token = int(expiry_token)

    def create(self,data:dict) -> str:
        """
        This function creates an API key using the provided data.
        
        :param data: The data parameter is the input data that will be used to create an API key. It could
        be any relevant information such as application details, or any other required information.
        """
        
        self.data = self.modify(
            data=data,
            expiry_token=self.expiry_token,
        )
        
        return engine.create(
            data=self.data,
            secret_key=self.api_secret_key,
            algorithm=self.algorithm
            )

    def read(self,token=None) -> str:
        """
        This function read the api key and return the list or dict.
        
        """
    

        data = engine.read({"token":token,
            "secret_key":self.api_secret_key,
            "algorithm":self.algorithm
        })
        if cte(data['expiry_time']) != True:
               return {
                   "error":401,
                   "message":"token expire"
                     }
        else:
            return data
        


    def modify(self,**args):
        data = args.get('data')
        now = datetime.datetime.now()
        # expire_date = today + datetime.timedelta(days=args.get("expiry_token"))
        expire_time = now + datetime.timedelta(seconds=args.get("expiry_token"))
        expire_time = expire_time.strftime("%H:%M:%S")
        
        data.update({
            "expiry_time": str(expire_time)
        })
        return data
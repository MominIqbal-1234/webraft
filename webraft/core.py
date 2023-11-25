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
from . import engine
from .process import ProcessToken
from .generator import GenerateKey


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

    def read(self, request, args:list=None,header=None) -> list or dict:
        
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


    

def generator():
    return GenerateKey.generate_key()




def PublicIP():
    return publicip()

def userIpinfo(request):
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

    # def device_is(self) -> str: return self.user_agent.device.family
    """
    This function returns the device family of a user agent.
    :return: The function `device_is` is returning user device
    user agent.
    """
        
    # def os_is(self) -> str:return self.user_agent.os.family
    """
    This function returns the operating system family of the user agent.
    :return: user operating system
    """
        
        
    # def browser_is(self) -> str:return self.user_agent.browser.family
    """
    This function returns the browser family of the user agent.
    :return: a string that represents the browser family of the user agent.
    """


    # def deviceIs(self) -> str:return self.user_agent.get_device()
        
    # def osIs(self) -> str:return self.user_agent.get_os()
        
    # def browserIs(self) -> str:return self.user_agent.get_browser()
       
    # def mobileIs(self) -> bool:return self.user_agent.is_mobile
        
    # def tabletIs(self) -> bool:return self.user_agent.is_tablet
      
    # def touchCapableIs(self) -> bool:return self.user_agent.is_touch_capable
        
    # def pcIs(self) -> bool:return self.user_agent.is_pc
        
    # def botIs(self) -> bool:return self.user_agent.is_bot
        
    # def emailClientIs(self) -> bool: return self.user_agent.is_email_client
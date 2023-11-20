try:
    from django.middleware import csrf
except:
    pass
import datetime
from . import engine


class ProcessToken:
    def modify(**args):
        data = args.get('data')
        today = datetime.datetime.now()
        expire_date = today + datetime.timedelta(days=args.get("expiry_token"))
        if args.get("framework") == 'django':
            data.update({
                "expiry_date": str(expire_date)[2:],
                "X-CSRFToken":csrf.get_token(args.get('request'))
            })
        else:
            data.update({
                "expiry_date": str(expire_date)[2:]
            })
        return data

    
    def dataList(kwargs):
        if len(kwargs.get('args')) != 0:
            values = engine.read(kwargs).get('data')
            return [values.get(i) for i in kwargs.get('args')]
        else:
            return engine.read(kwargs)
        
        
    def getHeader(self,**kwargs):
        try:
            self.kwargs = kwargs
            request = kwargs.get("request")
            if kwargs.get("framework") == 'fastapi' or 'flask' or 'bottle':
                self.kwargs.update({'token':request.headers[kwargs.get('header')]})
                return ProcessToken.dataList(self.kwargs)

            elif kwargs.get("framework") == 'django':  
                self.kwargs.update({'token':request.headers[kwargs.get('header')]})
                return ProcessToken.dataList(self.kwargs)
           
        except Exception as e:
            raise ValueError(e)
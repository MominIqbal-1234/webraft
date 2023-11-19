try:
    from django.middleware import csrf
except:
    pass
import datetime


class Modification:
    def modify(data,request,expiry_token,framework):
        today = datetime.datetime.now()
        expire_date = today + datetime.timedelta(days=expiry_token)
        if framework == 'django':
            data.update({
                "expiry_date": str(expire_date)[2:],
                "X-CSRFToken":csrf.get_token(request)
            })
        else:
            data.update({
                "expiry_date": str(expire_date)[2:]
            })
        return data
        
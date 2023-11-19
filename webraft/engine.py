import jwt



def create(data,secret_key,algorithum):
    try:
        return jwt.encode(data,secret_key, algorithm=algorithum)
    except Exception as e:
        raise ValueError(e)
        
def read(apikey,secret_key,algorithum):
    try:
        return jwt.decode(apikey, secret_key, algorithms=algorithum)
    except Exception as e:
        raise ValueError(e)
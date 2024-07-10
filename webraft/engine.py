import jwt



def create(**args):
    try:
        return jwt.encode(args.get('data'),args.get('secret_key'), algorithm=args.get('algorithm'))
            

    except Exception as e:
        raise ValueError({
            "status":404,
            "error":e
        })
        
def read(kwargs):
    try:
        return jwt.decode(kwargs.get("token"), kwargs.get("secret_key"), algorithms=kwargs.get("algorithm"))
    except Exception as e:
        raise ValueError({
            "status":404,
            "error":e
        })
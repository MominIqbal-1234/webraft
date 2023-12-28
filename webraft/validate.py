from datetime import datetime

__algorithm__ = [
    "HS256",
    "HS512",
    "RS256",
]

__framework__ = [
    
    "django",
    "flask",
    "fastapi",
    "bottle",

]

def validateAlgorithm(algorithm):
    if algorithm == None:
        raise ValueError("algorithm not define")
    elif algorithm not in __algorithm__:
        raise ValueError("support algorithm",__algorithm__)

def validateFramework(framework):
    if framework == None:
        raise ValueError("framework not define")
    elif framework not in __framework__:
        raise ValueError(f"framework support",__framework__)

def validateExpirytoken(expiry_token):
    if expiry_token == None:
        raise ValueError("Invalid Expire time")
    elif expiry_token <= 0:
        raise ValueError("0 expiry_token not valid")

def validateExpiryDate(data):
    check = list(data)
    value = [(i) for i in check if "expiry_time" == i]

    if value == []:
        return True
    if value[0] == "expiry_time":
        raise ValueError("expiry_date already exist")


def check_token_expiry(time:str):
    given_time_str = time

    given_time = datetime.strptime(given_time_str, "%H:%M:%S").time()
    today = datetime.now().date()
    given_datetime = datetime.combine(today, given_time)

    current_datetime = datetime.now()

    if current_datetime > given_datetime:
        return False
    elif current_datetime < given_datetime:
        return True
    else:
        return True
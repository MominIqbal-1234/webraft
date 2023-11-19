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
        raise ValueError("add token expire date")
    elif expiry_token <= 0:
        raise ValueError("0 expiry_token not valid")

def validateExpiryDate(data):
    check = list(data)
    value = [(i) for i in check if "expiry_date" == i]

    if value == []:
        return True
    if value[0] == "expiry_date":
        raise ValueError("expiry_date already exist")
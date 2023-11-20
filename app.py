from flask import Flask,request
from webraft.core import JWTToken


app = Flask(__name__)
token = JWTToken(
      secret_key='my_key',
      expiry_token=1,
      framework='flask',
      algorithm='HS256'
      )


@app.route("/")
def hello_world():
    print(type(request))
    token1 = token.create(request,{
        "username":"admin",
        "user_id":1
    })
    print(token1)
    return "Hello"

@app.route("/read")
def read():
    print(type(request))
    token1 = token.read(request,[
        "username",
        "id"
            ])
    print(token1)
    return "Hello"

if __name__ == "__main__":
	app.run(debug=True)
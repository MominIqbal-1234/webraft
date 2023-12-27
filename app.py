from flask import Flask,request
from webraft.core import JWTToken,generator,MetaData,APIKey
from flask import jsonify

app = Flask(__name__)
token = JWTToken(
      secret_key='my_key',
      expiry_token=60,
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
    return jsonify(token1)


@app.route("/read")
def read():
    print(type(request))
    token1 = token.read(request)
    # print(generator())
    return jsonify(token1)

@app.route("/meta")
def meta():
    device_is = MetaData(request,'flask').device_is
    browser_is = MetaData(request,'flask').browser_is
    print(device_is)
    return jsonify(device_is,browser_is)

if __name__ == "__main__":
	app.run(debug=True)
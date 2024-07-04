from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "username": "username"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def home():
    return jsonify(message="Hello, Secure and Password-Protected World!")

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))

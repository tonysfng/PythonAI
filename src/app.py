import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
print(os.getenv("system"))

@app.route("/", methods = ['Get', 'Post'])
def home():
    return 'OK', 200

def require_auth(f):
    def wrapper(*args, **kwargs):
        # Check authentication here
        return f(*args, **kwargs)
    return wrapper

@app.route('/secure')
@require_auth
def secure_area():
    return "This is a secure area." * 2


import re
from flask import Flask, json,jsonify, request
from newsapi import NewsApiClient
from flask_cors import CORS, cross_origin
import pyrebase
import pickle as pkl
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
###Initialize Firebase
secrets = {'apiKey': "AIzaSyDR8tFTYqMqSYI6K1HAjJBfeS774o3aU5o",
    'authDomain': "spaceblogs.firebaseapp.com",
    'projectId': "spaceblogs",
    'storageBucket': "spaceblogs.appspot.com",
    'messagingSenderId': "113377744070",
    'appId': "1:113377744070:web:60c5f3e34e25b60987b3c7",
    'measurementId': "G-PG3VEDCTC8",
    'databaseURL' : "https://spaceblogs-default-rtdb.asia-southeast1.firebasedatabase.app/"}
firebase = pyrebase.initialize_app(secrets)

###Initialize Firebase methods
auth = firebase.auth()
# database = firebase.database()
db = firebase.database()

### Home Route ###
@app.route('/')
@cross_origin()
def home():
    return "Welcome to space blogs!!"

### News Section ###
@app.route('/news')
@cross_origin()
def news():
    newsapi = NewsApiClient(api_key="2dd3b52f72744bedbec4d19810f86480") 
    top_headlines = newsapi.get_top_headlines(q='space',
                                          language='en')
    return jsonify(top_headlines)

### Blogs Route ###
@app.route('/blogs', methods=['GET','POST'])
@cross_origin()
def blogs():
    if request.method == "POST":
        try:
            urlToImage = request.json['urlToImage']
            title = request.json['title']
            author = request.json['author']
            content = request.json['content']
            description = request.json['description']
            publishedAt = request.json['publishedAt']
            data = {
                "urlToImage" : urlToImage,
                "title" : title,
                "author" : author,
                "content" : content,
                "description" : description,
                "publishedAt" : publishedAt,
                "status" : "pending"
            }
            db.child('blogs').push(data)
            return '1'
        except:
            return '0'
    else:
        blogs = db.child('blogs').get()
        res = {"articles": []}
        for i in blogs.val():
            if blogs.val()[i]["status"] == "approved":
                blogs.val()[i]["id"] = i
                res['articles'].append(blogs.val()[i])  
        return jsonify(res)

### Sign In/Out Section ###
@app.route('/signin', methods=['GET','POST'])
@cross_origin()
def signin():
    if request.method == "POST":
        try:
            email = request.json['email']
            password = request.json['password']
            user = auth.sign_in_with_email_and_password(email,password)
            userData = auth.get_account_info(user['idToken'])
            return jsonify({"email": userData['users'][0]['email'], "credential" : True})
        except:
            return jsonify({"email": "Invalid", "credential": False})
    else:
        return "Sign In API"

###Sigup section###
@app.route('/signup', methods=['GET','POST'])
@cross_origin()
def signup():
    if request.method == "POST":
        userEmail = request.json['email']
        userPassword = request.json['password']
        try:
            auth.create_user_with_email_and_password(userEmail, userPassword)
            return jsonify({"email": userEmail, "credential": True})
        except:
            return jsonify({"email": "userEmail", "credential": False})
    else:
        return "Sign Up API"

### Blog Post Route ###
@app.route('/blogpost', methods=['GET', 'POST'])
@cross_origin()
def blogpost():
    if request.method == "POST":
        blogId = request.json['id']
        blogs = db.child('blogs').get()
        return blogs.val()[blogId]
    else:
        return 'Blog Post API'

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
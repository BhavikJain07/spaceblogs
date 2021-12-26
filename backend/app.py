from flask import Flask,jsonify, request
from newsapi import NewsApiClient
from flask_cors import CORS, cross_origin
import pyrebase
import pickle as pkl
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
###Initialize Firebase
secrets = {}
with open('secrets.dat','rb') as f:
    secrets = pkl.load(f)
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
        userName = request.json['username']
        blogContent = request.json['blog']
        data = {
            "author": userName,
            "content": blogContent,
            "status" : "pending"
        }
        db.child('blogs').push(data)
        return '1'
    else:
        blogs = db.child('blogs').get()
        BLOGS = {}
        for i in blogs:
            if i.val()['status'] == "approved":
                BLOGS[i.key()] = i.val()
        return jsonify(BLOGS)

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

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
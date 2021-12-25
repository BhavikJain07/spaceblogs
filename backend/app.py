from flask import Flask,jsonify, request
from newsapi import NewsApiClient
import pyrebase
import pickle as pkl
app = Flask(__name__)

###Initialize Firebase
secrets = {}
with open('secrets.dat','rb') as f:
    secrets = pkl.load(f)
firebase = pyrebase.initialize_app(secrets)

###Initialize Firebase methods
auth = firebase.auth()
# database = firebase.database()
db = firebase.database()

###Home Route###
@app.route('/')
def home():
    return "This is not your place to be! Get Lost!!"

###News Section ###
@app.route('/news')
def news():
    newsapi = NewsApiClient(api_key="2dd3b52f72744bedbec4d19810f86480") 
    top_headlines = newsapi.get_top_headlines(q='space',
                                          language='en',
                                          category="technology")
    return jsonify(top_headlines)

###Blogs Route###
@app.route('/blogs', methods=['GET','POST'])
def blogs():
    if request.method == "POST":
        userName = request.args['username']
        blogContent = request.args['blog']
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

###Sign In/Out Section###
@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == "POST":
        userEmail = request.args['email']
        userPassword = request.args['pass']
        try:
            auth.sign_in_with_email_and_password(userEmail, userPassword)
            return '1'
        except:
            return '0'
    else:
        return "Sign In API"

###Sigup section###
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        userEmail = request.args['email']
        userPassword = request.args['pass']
        try:
            auth.create_user_with_email_and_password(userEmail, userPassword)
            return '1'
        except:
            return '0'
    else:
        return "Sign Up API"

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
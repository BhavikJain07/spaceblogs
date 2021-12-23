from flask import Flask,jsonify, request, render_template
from newsapi import NewsApiClient
app = Flask(__name__)

###Home Route###
@app.route('/')
def home():
    return render_template('index.html')

###News Section ###
@app.route('/news')
def news():
    newsapi = NewsApiClient(api_key="2dd3b52f72744bedbec4d19810f86480") 
    top_headlines = newsapi.get_top_headlines(q='space',
                                          language='en',
                                          category="technology")
    return jsonify(top_headlines)

###Blogs Route###
@app.route('/blogs')
def blogs():
    return 'Blogs here'

###Sign In/Out Section###
@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == "GET":
        name = request.args['id']
        return name
    else:
        return "Hello"

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
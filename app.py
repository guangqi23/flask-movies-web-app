from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)
app.config['DEBUG'] = True


# /watch from Youtube is a unique route name, unique paths
@app.route("/")
def show_landing_page():
    try:
        # all of the html files need to be under 'templates' directory
      
        return render_template('landing-page.html', name='Heicoders')
    except:
        return '<h1> An error occured! </h1>'


# Login Page
@app.route("/login")
def login():
 return "Welcome to our login page"

# Search Page, because we're using POST in our front-end page.
@app.route("/search", methods=['POST'])
def form_submit():
    user_query = request.form['search_query'] # The item from the landing-page.html
    print(user_query) # Whatever the user typed 

    # Trying to look for the function which is below def search_imdb, must match function name!
    redirect_url = url_for('.search_imdb', query_string=user_query)
    print(redirect_url)
    return redirect(redirect_url)

@app.route("/search/<query_string>", methods=['GET'])

def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q": query_string}

    headers = {
        'x-rapidapi-key': "7406ce2570msh2cdf4c78aab3a28p12fc39jsn3be65634f33e",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template('search-result.html', data=data)
    except:
        return render_template('error404.html')
 
# Error Handling Page
@app.route("/error")
def return_error():
 return render_template('error404.html')


# Another Example of a Dynamic Routing
@app.route("/watch/<video_id>")
def watch_video(video_id):
 return "Video ID " + video_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

# 0.0.0.0 is 'localhost', so 0.0.0.0:5000 is using Flask Server
# Heroku will need us to write them down in 0.0.0.0
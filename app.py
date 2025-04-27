from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://official-joke-api.appspot.com/random_joke')
joke = response.json()

@app.route('/')
def home():
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)

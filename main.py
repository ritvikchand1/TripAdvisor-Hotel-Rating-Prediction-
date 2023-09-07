from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def render_home():
   return render_template('index.html')

@app.route("/submit_input_text", methods = ['GET', 'POST'])
def process_input():
    input = request.get_json()
    print(input)
    print(input['text'])
    return input['text']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)
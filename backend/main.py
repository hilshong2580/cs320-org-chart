from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'todo: everything'

app.run(debug=True)
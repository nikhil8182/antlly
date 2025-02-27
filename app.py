from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')




if __name__ == '__main__':
    # Development
    app.run(debug=True, port=5001)
else:
    # Production
    app.config['DEBUG'] = False

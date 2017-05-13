from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def homepage ():
    return render_template('index.html')

@application.route('/layout')
def layout ():
    return render_template('layout.html')

if __name__ == "__main__":
    application.debug = False
    application.run()

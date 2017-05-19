from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def homepage ():
    return render_template('index.html')

@application.route('/pricing', methods=['GET', 'POST'])
def pricing ():
    return render_template('pricing.html')

if __name__ == "__main__":
    application.debug = False
    application.run()

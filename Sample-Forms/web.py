from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')

    return render_template('thankyou.html',name=name)

@app.errorhandler(404)
def error(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
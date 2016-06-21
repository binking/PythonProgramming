from flask import Flask
from flask import request

my_app = Flask(__name__)

@my_app.route('/', methods=['GET', 'POST'])
def home():
    return b"<H1>Hello, this is home page !</H1>"

@my_app.route('/signin', methods=['GET'])
def sign_in_form():
    return b"""
            <H1>Sign In<H1>
            <form action="/signin" method="POST">
            <p><input name="username"></p>
            <p><input name="userpasswd" type="password"></p>
            <p><button type="submit">Sign In</button></p>
            """

@my_app.route('/signin', methods=['POST'])
def sign_in_process():
    if request.form['username'] == "admin" and request.form['userpasswd'] == 'admin':
        return "Welcome back, Admin!"
    return "<H3>Bad user or password !<H3>"

if __name__=="__main__":
    my_app.run()

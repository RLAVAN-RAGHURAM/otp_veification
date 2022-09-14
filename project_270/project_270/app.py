# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login',method=['POST'])
def verify_otp():
    username=request.form['username']
    password=request.form['password']
    mobile_number=request.form['number']
    if username=='verify' and password=='12345'
        account_sid="IS174a159f9d11e547e003d859d8baaa70"
        auth_token="IS174a159f9d11e547e003d859d8baaa70"
        client=Client(account_sid,auth_token)
        services('IS174a159f9d11e547e003d859d8baaa70')
        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=mobile_number, channel='sms')
        print(verification.status)
        return render_template('otp_verify.html')
    else:
        print("Given User ID Or Password Is Wrong")










if __name__ == "__main__":
    app.run()


#import libraries
from flask import Flask,render_template,jsonify,request
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant



app = Flask(__name__)
#write code here
fake=Faker()

@app.route('/')
def index():
    return render_template('index.html')


#write code here
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID="ACc07131165619ddab29e35e673d392f32"
    TWILIO_SYNC_SERVICE_SID="IS174a159f9d11e547e003d859d8baaa70"
    TWILIO_API_KEY="SK00f9290d1997147f3f91ce618d24cd68"
    TWILIO_API_SECRET="T8mcpeSbQuTMK4ZcskTFZXNAC1i88zag"

    username=requet.args.get("username",fake.user_name())

    token=AccessToken(TWILIO_ACCOUNT_SID,TWILIO_API_KEY,TWILIO_API_SECRET,identity=username)
    sync_grant_access=SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username,token=token.to_jwt())





if __name__ == "__main__":
    app.run()


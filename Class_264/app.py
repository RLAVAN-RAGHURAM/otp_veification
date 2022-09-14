# Program to Upload Color Image and convert into Black & White image
import os
import cv as Opencv
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory



app = Flask(__name__)

# Write load_form function below to Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')




@app.route('/gray',methods=['POST'])
# Write upload_image Function to upload image and redirect to new webpage
def upload_image():
    file=request.files['file']
    filename=secure_filename(file.filename)
    d=os.path.join( "C:/Users/raghu/Documents/Cloud/Class_264/static/",filename)
    print(d)
    x=file.save(d)
    print(x)
    display_message="Image successfully uploaded and displayed below"
    return render_template('upload.html',filename=filename,message=display_message)




# Write display_image Function to display the uploaded image
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static',filename=filename))

@app.route('/static/<filename>')
def send_report(filename):
    return send_from_directory("C:/Users/raghu/Documents/Cloud/Class_264/static/", filename)


if __name__ == "__main__":
    app.run()
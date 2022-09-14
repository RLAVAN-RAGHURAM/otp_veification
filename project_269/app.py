# Import Libraries
import os
from flask import Flask, render_template, request, redirect, url_for, send_file




# Initilize the Flask
app=Flask(__name__)



# Route and define the index function to render the home.html.
@app.route('/')
def upload_form():
    return render_template('home.html')



# Call the app.run()
if __name__ == "__main__":
    app.run()



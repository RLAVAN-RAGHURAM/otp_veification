from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def upload_html():
	print("HTML Page Is Loaded")
	return render_template('index.html')

if __name__=="__main__":
	app.run()
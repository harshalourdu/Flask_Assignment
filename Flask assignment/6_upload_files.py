# 6. Build a Flask app that allows users to upload files and display them on the website.



from distutils.log import debug 
from fileinput import filename 
from flask import *
app = Flask(__name__) 

@app.route('/') 
def main(): 
	return render_template("upload.html") 

@app.route('/success', methods = ['POST']) 
def success(): 
	if request.method == 'POST': 
		f = request.files['file'] 
		f.save(f.filename) 
		return render_template("Acknowledgement.html", name = f.filename) 

if __name__ == '__main__': 
	app.run(host="0.0.0.0" , port=5000)

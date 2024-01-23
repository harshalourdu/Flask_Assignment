# 10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template 
  
app = Flask(__name__) 
  
# app name 
@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e): 
  
# defining function 
  return render_template("404.html") 

if __name__ == '__main__':
	app.run(host="0.0.0.0" , port=5000)
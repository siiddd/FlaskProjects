#Import Packages
from flask import Flask 

#Create an instance
app = Flask(import_name = '__name__')

#Create a path
@app.route('/preethan') # http://127.0.0.1/5000/preethan

#Core Program
def bot():
    return 'Hello Sid!'

#Run the Program
if __name__ == "__main__":
    app.run()


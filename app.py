students = {
            '18pt01':{
                        'name' : 'name1',
                        'class' : '18pt'
                       },
            '18pd01':{
                        'name' : 'name2',
                        'class' : '18pd'
                       }
            }
    
    

from flask import Flask

app = Flask(__name__)

@app.route("/students") 
def hello_world():
    return students

@app.route("/18pd01") 
def hello_world1():
    return students 
if __name__ == "__main__":
    app.run()
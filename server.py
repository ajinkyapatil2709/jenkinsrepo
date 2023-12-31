from flask import Flask

# create flask app
app = Flask(__name__)

courses = ['FCN',
           ' COSA',
            'SECURITY CONCEPTS',
            'ITIM & DEVOPS',
            'NDC',
            'PKI',
            'CYBER FORENSICS',
           ' COMPLIANCE AUDIT', 
           ' APPTITUDE and EFFECTIVE COMMUNICATION' 
            ' Checked by Gajanan Sir.'  
          ]
name = [ 'Name : Ajinkya Patil' , 'Course : PG-DITISS', ' PRN : 230344223002', 'PHONE NUMBER : 8888407020']
# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL EXAM"

@app.route("/modules", methods=["GET"])
def get_list():
    return courses

@app.route("/me", methods=["GET"])
def name():
    return name



# run the application
app.run(host="0.0.0.0", port=4000, debug=True)

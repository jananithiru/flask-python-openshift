from flask import Flask
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__);

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rupalighc2017@gmail.com'
app.config['MAIL_PASSWORD'] = 'test123$'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app);


def sendEmail(emailFrom, emailTo, msgStr):
	with app.app_context():
		try:
			print ("Email setup done!");
			msg = Message(msgStr, sender=emailFrom, recipients=[emailTo]);
			msg.body = "Test Body";
			mail.send(msg);
			print("Sent the email message");
		except ValueError:
			print("Error while sending email!");



sendEmail("rupalighc2017@gmail.com", "rupalighc2017@gmail.com", "Message - Volunteer found!");

if __name__ == '__main__':
   app.run(debug = True)
	

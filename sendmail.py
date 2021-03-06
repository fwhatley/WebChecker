import sendgrid
import os
from sendgrid.helpers.mail import *


def sendemail(recipient, emailSubject, body):
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	from_email = Email("heroku@myapp.com")
	to_email = Email(recipient)
	content = Content("text/plain", body)
	mail = Mail(from_email, emailSubject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())

	print("### Email sent to: "+ recipient + " ###")
	print(response.status_code)
	print(response.body)
	print(response.headers)

	

if __name__ == "__main__":
	sendemail('rwhat357@hotmail.com', "hello world", "you have mail from heroku from Fredy!")
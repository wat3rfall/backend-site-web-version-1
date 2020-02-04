from flask import Flask, render_template, request, redirect
import smtplib, ssl
import email
import os


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("pages/home.html")


@app.route("/form-requests", methods=["GET", "POST"])
def form_requests():
	if request.method == "POST":
		print(request.form)

		port = 587
		smtp_server = "smtp.gmail.com"
		sender_email = os.environ["SENDER_EMAIL"]
		receiver_email = os.environ["RECEIVER_EMAIL"]
		password = os.environ["SENDER_PASSWORD"]

		message = """\
		<b>Auteur:</b> %s<br>
		<b>Courriel:</b> %s<br>
		<b>Sujet:</b> %s<br><br>

		<b>Message:</b>
		%s
		""" %(request.form["nom"], 
			request.form["courriel"], 
			request.form["sujet"], 
			request.form["message"])

		# message = message.encode("utf-8")

		msg = email.message.Message()
		msg['Subject'] = "Requête de contact du site web"
		msg['From'] = sender_email
		msg['To'] = receiver_email
		msg.add_header('Content-Type','text/html')
		msg.set_payload(message)


		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
			server.ehlo()
			server.starttls(context=context)
			server.ehlo()
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, msg.as_string().encode("utf-8"))

			message = request.form["message"]
		return render_template("pages/success_fr.html")

	return "Page not found"

if __name__ == "__main__":
	app.run()

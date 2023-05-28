import os
import requests
from dotenv import load_dotenv
import jinja2
load_dotenv()
domain = os.getenv("MAILGUN_DOMAIN")
api_key = os.getenv("MAILGUN_API_KEY")

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_name, **kwargs):
    template = template_env.get_template(template_name)
    return template.render(**kwargs)

def send_simple_message(to, subject, body, html):
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", api_key),
		data={
            "from": f"Store Owner <mailgun@{domain}>",
			"to": [to],
			"subject": subject,
			"text": body,
            "html": html
            }
        )

def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/action.html", username=username)
    )
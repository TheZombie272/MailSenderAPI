from flask import Flask, request, jsonify, app
from mailersend import emails
from dotenv import load_dotenv
import os


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def send_email():

    data = request.get_json()

    load_dotenv()

    mailer = emails.NewEmail(os.getenv('MAILERSEND_API_KEY'))

    # define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": os.getenv('NAME'),
        "email": os.getenv('EMAIL'),
    }


    reply_to = {
        "name": "Name",
        "email": "a@a.a",
    }

    template = select_template(data)


    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(data['reciepient'], mail_body)
    mailer.set_subject(data['subject'], mail_body)
    mailer.set_html_content(template, mail_body)
    mailer.set_plaintext_content(data['content'], mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    # using print() will also return status code and data
    print(mailer.send(mail_body))
    return jsonify({"message": "User updated successfully"}), 202


def select_template(data):
    template_name = data['template']
    if template_name == '2-fa':
        with open('models/2-fa.html', 'r') as f:
            template = f.read()
    print(data['reciepient'][0]['name'])
    template = template.replace('{{name}}', data['reciepient'][0]['name'])
    template = template.replace('{{code}}', data['content'])

    return template


"""
example of petition

{
    "reciepient":[
        {
            "name": "a",
            "email": "a@gmail.com"
        },
        {
            "name": "b",
            "email" : "b@gmail.com"
        }
    ],
    "subject": "this it the subject",
    "content": "this is the content",
    "template": "2-fa"
}

"""





if __name__ == '__main__':
  app.run(debug=True)
from smtplib import SMTP_SSL
from email.message import EmailMessage
import re

def main(args):
    try:
        validate_args(args)
    except AssertionError as ex:
        return {
            'Error': 'Argument validation failed'
        }

    try:
        sendmail(args)
    except Exception:
        return {
            'Error': 'Sending Mail failed!',
            'Exception': ex.message
        }

    return {'Success': "Mail sent."}

def sendmail(args):
    message = EmailMessage()
    message['To'] = args['to']
    message['From'] = args['smtp_from']
    message['Subject'] = args['subject']
    message.set_content(args['body'])
    
    smtp = SMTP_SSL(args['smtp_host'], int(args['smtp_port']))
    smtp.login(args['smtp_user'], args['smtp_password'])
    smtp.send_message(message)
    smtp.quit()

def validate_args(args):
    assert 'smtp_host' in args
    assert 'smtp_port' in args
    assert 'smtp_from' in args
    assert 'smtp_user' in args
    assert 'smtp_password' in args
    assert 'to' in args
    assert 'subject' in args
    assert 'body' in args
    assert args['smtp_host']
    assert args['smtp_port']
    assert args['smtp_from']
    assert args['smtp_user']
    assert args['smtp_password']
    assert args['to']
    assert args['subject']
    assert args['body']
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", args['to']) is None:
        raise AssertionError()

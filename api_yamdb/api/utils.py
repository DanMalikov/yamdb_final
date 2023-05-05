
from django.core.mail import EmailMessage

DOMAIN_NAME = 'test'


def send_email(user):
    email_body = (
        f'Доброе время суток, {user.username}.'
        f'\nКод подтверждения для доступа к API: {user.confirmation_code}'
    )
    data = {
        'email_body': email_body,
        'to_email': user.email,
        'email_subject': 'Код подтверждения для доступа к API!'
    }
    email = EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        to=[data['to_email']],
        from_email='yambd@' + DOMAIN_NAME + '.ru'
    )
    email.send()

# utils/email.py
from django.core.mail import send_mail

def mock_send_email(subject, message, from_email, recipient_list, fail_silently=False):
    print("Mock email sent:")
    print("Subject:", subject)
    print("Message:", message)
    print("From:", from_email)
    print("To:", recipient_list)

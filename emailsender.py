import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  #same as os.path but pathlib is better

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'johndoe@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'john'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('johndoe429@gmail.com', 'gdaxhwrd') #insert email and password acesscode here
    smtp.send_message(email)
    print('email sent!')
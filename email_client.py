import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class EmailClient:
    def __init__(self, email_config):
        self.host = email_config['host']
        self.port = email_config['port']
        self.username = email_config['username']
        self.password = email_config['password']
        self.sender = email_config['sender']
        self.recipients = email_config['recipients']

    def send_email(self, subject, text_body=None, html_body=None, attachments=None, images=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)

        if text_body:
            msg.attach(MIMEText(text_body, 'plain'))
        if html_body:
            msg.attach(MIMEText(html_body, 'html'))

        if attachments:
            for attachment in attachments:
                with open(attachment, 'rb') as f:
                    attachment_data = MIMEApplication(f.read(), _subtype='octet-stream')
                    attachment_data.add_header('Content-Disposition', 'attachment', filename=attachment)
                    msg.attach(attachment_data)

        if images:
            for image in images:
                with open(image, 'rb') as f:
                    image_data = MIMEImage(f.read())
                    image_data.add_header('Content-ID', '<{}>'.format(image))
                    msg.attach(image_data)

        try:
            with smtplib.SMTP_SSL(self.host, self.port) as smtp:
                smtp.login(self.username, self.password)
                smtp.sendmail(self.sender, self.recipients, msg.as_string())
            print('Email sent successfully.')
        except Exception as e:
            print('Error sending email:', e)

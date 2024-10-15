import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipients):
    # Email configuration
    sender_email = 'candidlpd@gmail.com'
    sender_password = 'bbzy chvi puem nwat'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Set up the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send email to each recipient
        for recipient in recipients:
            # Create a new MIMEMultipart email for each recipient
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient
            message['Subject'] = subject

            # Add the email body
            message.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(sender_email, recipient, message.as_string())
            print(f'Email sent to {recipient}')

        # Close the SMTP server
        server.quit()

    except Exception as e:
        print(f'Failed to send email: {e}')

# List of recipients
recipients = ['dangal76053@gmail.com', 'ibanath.dangal@gmail.com']

# Email details
subject = 'Test Email'
body = 'This is a test email sent using Python.'

# Send the email
send_email(subject, body, recipients)

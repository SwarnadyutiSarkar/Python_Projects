import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

def read_data(file_path):
    """Reads data from a CSV file."""
    return pd.read_csv(file_path)

def generate_report(data):
    """Generates a report from the data."""
    today = datetime.today().strftime('%Y-%m-%d')
    report = data.describe()
    report_str = report.to_string()
    
    return f"Daily Report for {today}\n\n" + report_str

def send_email(report, to_email, from_email, password):
    """Sends an email with the report."""
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Report"
    
    msg.attach(MIMEText(report, 'plain'))
    
    # Connecting to the Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    data_file = 'data.csv'
    to_email = 'recipient@example.com'  # Change this to the recipient's email address
    from_email = 'your-email@gmail.com'  # Change this to your email address
    password = 'your-email-password'  # Change this to your email password
    
    data = read_data(data_file)
    report = generate_report(data)
    send_email(report, to_email, from_email, password)
    print("Email sent successfully.")

if __name__ == "__main__":
    main()

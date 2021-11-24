import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) # connection object that connects to the SMTP server
# usually port 587 see sending emails video for other ports

print(conn.ehlo()) # starts connection

print(conn.starttls()) # starts tls encryption to encrypt messages

print(conn.login('smallet079@gmail.com','Reconstruct8'))

print(conn.sendmail('smallet079@gmail.com','smallet079@gmail.com','Subject: So long...\n\nDear sam,\nSo long, and thanks for all the fish.\n\n-Sam'))
# ('send from email','send to email','body') returns any email that failed to send

conn.quit # disconnects you from the SMTP server

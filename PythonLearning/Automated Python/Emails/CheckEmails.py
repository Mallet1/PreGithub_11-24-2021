import imapclient, pyzmail
# https://imapclient.readthedocs.io/en/2.2.0/# for help with imap
# http://magiksys.net/pyzmail/ for help with pyzmail

conn=imapclient.IMAPClient('imap.gmail.com',ssl=True) # connection object that connects to the SMTP server
# ssl is the encryption algorithm

print(conn.login('smallet079@gmail.com','Reconstruct8'))

conn.select_folder('INBOX',readonly=True) # folder is usually INBOX
# readonly is True so you don't accidentally delete emails

# print(conn.list_folder()) to find other folders to search through

UIDs = conn.search(['Since','25-Mar-2021']) # https://gist.github.com/martinrusev/6121028 for search criteria
# (['TEXT','Maniaplanet'])
print(UIDs)

rawMessage=conn.fetch([UIDs[10]],['BODY[]','FLAGS'])

message=pyzmail.PyzMessage.factory(rawMessage[UIDs[10]][b'BODY[]']) # gets the message at the UID code
print(message.get_subject()) # gets the subject of the message
print(message.get_addresses('from')) # [('sender','their email')]
print(message.get_addresses('to')) # [('reciever','their email')]
print(message.get_addresses('bcc')) # emails included

print() # HTML email doesn't have just text

print(message.text_part) # checks if it has a text part
print(message.html_part) # checks if it has an html part

print()
print(message.text_part.charset) # to find the encoding the email was sent as
print()

print(message.text_part.get_payload().decode('UTF-8')) # to get body
# most of the time just pass UTF-8 to the encoding

# conn.select_folder('INBOX', readonly=False)
# UIDS=conn.search(['ON', '26-Mar-2021'])
# conn.delete_messages(UID) to delete a message

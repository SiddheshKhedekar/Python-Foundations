"""
The program that allows user to send a message from his personal computer to his mobile phone number however you need to register on twilio.com and get your first free number. However currently India is not supported so messages are undelivered. But sending messages this way is possible.
"""

# Client from python 3.5 = TwilioRestClient from python 2.7
from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC02152890984f17f8931b56bbe9730bdd"
# Your Auth Token from twilio.com/console
auth_token  = "ce0a808e561602c7a64c9350f8c10848"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+918976855865",    # replace with your phone number
    from_="+13188552648", # replace with your twilio number
    body="Your Phone has been Hacked! ----By SK") # message

print(message.sid)

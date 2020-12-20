from twilio.rest import Client

account_sid = 'AC8745cfc5ce453914484b59c9ad409fc6'
auth_token = '0619ecc1f5d8368d6ab1ef4ae4d1b2f4'
client = Client(account_sid, auth_token)

def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='hi',
        to='whatsapp:+919783508295'
    )

    print(message.sid)
from twilio.rest import Client

account_sid = 'AC4351767a2b0d36d633f610f7150aa3b4'
auth_token = '27c92cb430979402ce9afacdc041be20'
client = Client(account_sid, auth_token)

def send():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='hi',
       to='whatsapp:+919783508295'
   )

   print(message.sid)

##################################################

def wish():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='You are the sunshine of my life. And I am wishing you a very nice day because, for me, your happiness means so much, Stay happy. Your love gives me strength and motivate me. I am sending my love to you on this beautiful day.\n',
       to='whatsapp:+919783508295'
   )

   print(message.sid)

##################################################

def monday():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='Today is Monday. Get up You have to become a early riser\n',
       to='whatsapp:+919783508295'
   )

   print(message.sid)
##########################################
def tuesday():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='Today is Tuesday. Get up You have to become a early riser\n',
       to='whatsapp:+919783508295'
   )

   print(message.sid)
#############################################
def wednesday():
       message = client.messages.create(
           from_='whatsapp:+14155238886',
           body='Today is Wednesday. Get up You have to become a early riser\n',
           to='whatsapp:+919783508295'
       )

       print(message.sid)
############################################
def thursday():
       message = client.messages.create(
           from_='whatsapp:+14155238886',
           body='Today is Thursday. Get up You have to become a early riser\n',
           to='whatsapp:+919783508295'
       )

       print(message.sid)
############################################
def friday():
       message = client.messages.create(
           from_='whatsapp:+14155238886',
           body='Today is Friday. Get up You have to become a early riser\n',
           to='whatsapp:+919783508295'
       )

       print(message.sid)
############################################
def saturday():
       message = client.messages.create(
           from_='whatsapp:+14155238886',
           body='Today is Saturday. Get up You have to become a early riser\n',
           to='whatsapp:+919783508295'
       )

       print(message.sid)
############################################
def sunday():
       message = client.messages.create(
           from_='whatsapp:+14155238886',
           body='Today is Sunday. Get up You have to become a early riser\n',
           to='whatsapp:+919783508295'
       )

       print(message.sid)
############################################
def alarm():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='Wake up, Wake up. Its 7 already!!! ',
       to='whatsapp:+919783508295'
   )

   print(message.sid)
def step1():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='Get set ready for study',
       to='whatsapp:+919783508295'
   )

   print(message.sid)
def step2():
   message = client.messages.create(
       from_='whatsapp:+14155238886',
       body='Get set ready for Competitive Programming',
       to='whatsapp:+919783508295'
   )

   print(message.sid)

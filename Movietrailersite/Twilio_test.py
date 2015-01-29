from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfeddf15396e26552fdf0faf4beed1b15"
auth_token  = "6f4458689010d333ac138bb835fc7461"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! Yay! I love you <3",
    to="++15402292585",    # Replace with your phone number +1 540-999-4555
    from_="+15409994555") # Replace with your Twilio number
print (message.sid)
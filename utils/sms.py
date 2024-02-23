import africastalking

# Initialize Africa's Talking SMS
username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(recipient, message, sender="YOUR_SENDER_ID"):
    recipients = [recipient]

    try:
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"SMS sending failed: {str(e)}")
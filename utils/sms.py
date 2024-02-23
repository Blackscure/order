import africastalking

# Initialize Africa's Talking SMS
username = "sandbox"
api_key = "561540b277bad8b28de5e2aebee8463a1191c0c2f0371d8ece6398461a3255ae"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(recipient, message, sender="7898"):
    recipients = [recipient]

    try:
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"SMS sending failed: {str(e)}")
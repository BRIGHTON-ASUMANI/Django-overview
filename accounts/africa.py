# works with both python 2 and 3
import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "brighton"
        self.api_key = "18696560f647f921b072950f4ef9e5c24a76e583ec26b6ceb4f2ef6d34403daa"
        # Initialize the SDK
        africastalking.initialize(self.username,self.api_key)
        # Get the SMS service
        self.sms = africastalking.SMS

    def send_sms(self,message):
        # Set the numbers you want to send to in international format
        recipients = ["+254791862354"]

        # And send the SMS
        try:
			# That’s it, hit send and we’ll take care of the rest
            response = self.sms.send(message, recipients)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send_sms('welcome new user')
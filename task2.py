from flask import Flask, request
from email_validator import validate_email
import africastalking
import re

#launching the USSD app 
app = Flask(__name__) 

#initializing variables
sms = africastalking.SMS
username = "sandbox"
apikey = "xxxxxxxxxx"

africastalking.initialize(username, apikey)

#Initialize the SDK
sms = africastalking.SMS
recipients = ['+254728420195']
message = "Account registered succesfully!"
 
#stating the method POST and GET
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
global response

#APIs from Africastalking

session_id = request.values.get("sessionId", None)
 service_code = request.values.get("serviceCode", None)
 phone_number = request.values.get("phoneNumber", None)
 text = request.values.get("text", "default")

#prompt the customer to enter both the email and phone number
 if text == ' ':
    response  = "CON enter your email folowed by your phone number\n"
  
  elif text == 'text':
    email, phone = line.split()
      
  #should validate email and phone number
  def confirm_email(email): 
    try:
      email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email)
      phone = re.match(r^"[0-9]", phone)
        if match:
           
           #send an SMS approving the email and number format
           sms.send (message)  
    else:
        return "Incorect email or number format!"
     confirm_email ()
     
 return response
 
 If __name__ == ‘__main__’:
    app.run (True)
 

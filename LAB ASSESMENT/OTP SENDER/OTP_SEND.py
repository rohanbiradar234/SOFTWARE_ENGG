from email.message import EmailMessage
import random
import Sender_data
import smtplib

class otp_sender:
    def __init__(self):
        self.receiver_email = ''
        self.size = 4

    # Set receiver email
    def set_receiver_email(self, receiver_email):
        self.receiver_email = receiver_email

    # Set size of OTP
    def set_otpSize(self, size):
        if(size < 4 or size > 8):
            raise ValueError("OTP size should be between 4 and 8")
        self.size = size

    # Function to generate OTP
    def generateOTP(self):
        self.Otp = ""
        for i in range(self.size):
            self.Otp += str(random.randint(0, 9))

    # Function to verify OTP
    def verifyOTP(self, otp_1):
        if otp_1 == self.Otp:
            return True
        else:
            return False

    # Function to send OTP through email
    def sendOTP(self):
        # Get sender's details
        sender_email = Sender_data.email
        sender_password = Sender_data.password

        # creating an object of EmailMessage class
        msg = EmailMessage()

        # Defining email subject, sender email, receiver email & email body
        msg['Subject'] = "One Time Password"
        msg['From'] = sender_email
        msg['To'] = self.receiver_email
        msg.set_content(str(self.Otp)+" is your OTP")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # Login to SMTP server
            server.login(sender_email, sender_password)

            # Sending email using send_message method by passing EmailMessage object
            server.send_message(msg)

            # Disconnect server
            server.quit()


if __name__ == '__main__':
    # Create an object of class otp_sender
    OTP = otp_sender()

    # Get receiver's email
    receiver_email = input("Enter your email: ")
    OTP.set_receiver_email(receiver_email)

    # Get size of otp
    size = int(input("Enter length of OTP: "))
    OTP.set_otpSize(size)

    # generate OTP
    OTP.generateOTP()

    # Send OTP
    OTP.sendOTP()
    print("OTP sent!")

    # Verify OTP
    otp_1 = input("Enter your OTP: ")

    if OTP.verifyOTP(otp_1):
        print("Verified!")
    else:
        print("Incorrect OTP!")
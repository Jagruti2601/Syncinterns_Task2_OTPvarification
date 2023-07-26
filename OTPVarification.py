import random

def generate_otp():
    # Generate a 6-digit OTP
    return str(random.randint(100000, 999999))

def send_otp_via_email(email, otp):
    # Code to send the OTP to the user's email
    print(f"Sending OTP {otp} to {email}")

def verify_otp(entered_otp, generated_otp):
    # Compare the entered OTP with the generated OTP
    return entered_otp == generated_otp

# Example usage
email = "user@example.com"

# Generate OTP and send it via email
otp = generate_otp()
send_otp_via_email(email, otp)

# Prompt the user to enter the OTP
entered_otp = input("Enter the OTP: ")

# Verify the entered OTP
if verify_otp(entered_otp, otp):
    print("OTP verified successfully!")
else:
    print("Invalid OTP. Please try again.")


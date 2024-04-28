import smtplib

my_email = "buzinov.yura@gmail.com"
password = "xxxx xxxx xxxx xxxx"

subject = "Subject:Test Title\n\n"
body = "This the body of my email.\nSecond Line\n\tThird Line" \
          "\nNext row of message"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() # start transport layer security | make our connection secure
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
# connection.close()

# 👆👆👆 this is same code

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"{subject}{body}")

# This is an example of a message you might receive.
message = "LKP9D1F6EP Confirmed. Ksh20.00 sent to PesaPal  for account 0772320009 on 25/11/17 at 9:24 AM New M-PESA balance is Ksh1,010.16. Transaction cost, Ksh0.00."

# save the contents into a list of words
content = message.split(" ")

# assuming messages of particular kind are uniform you might read them as follows:
# otherwise you might have to integrate mpesa API
mpesaid = content[0]
amount = content[2][3:]
sent_to = content[5]
account = content[9]
date = content[11]
time = content[13]+content[14]
balance = content[19][3:-1].replace(",","")


data = {
    "mpesaid":mpesaid,
    "amount":amount,
    "sent_to":sent_to,
    "account":account,
    "date":date,
    "time":time,
    "balance":balance
}
print(data)

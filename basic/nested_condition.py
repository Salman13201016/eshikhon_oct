

name = "salman1"
phone = "01705644008"
email = "s"

if(len(name) == 0 or len(phone)==0 or len(email)==0): 
    status = "failed"
    print(status)

else:
    if(len(name)<2 or len(name)>6):
        print("the name length must be between 2 and 6")
    elif(len(phone)!=11):
        print("the phone number size must be equal to 11")
    else:
        print("success")


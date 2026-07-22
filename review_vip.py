age = int(input("سن خود را وارد کنید"))
spacial_member = input("ایا عضو ویژه هستید؟ yes or no ")
has_ticket =input("ایا بلیت دارید؟ yes or no")
if age >=18 and (spacial_member =="yes" or has_ticket == "yes") :
    print("ورود مجاز است")
else :
    print("ورود غیر مجازاست")

age = int(input("سن خود را وارد کنید:"))
has_ticket = input("ایا بلیت دارید؟ yes یا no :") 
if age >= 18 and has_ticket == "yes":
    print("می توانید وارد شوید")
else:
    print("نمی توانید وارد شوید")
    
age = int(input("سن خود را وارد کنید: "))
has_ticket = input("ایا بلیت دارید؟:(yes یا no) ")
if age >=18 and has_ticket == "yes":
    print("ورود مجاز است")
else:
    print("ورود مجاز نیست")


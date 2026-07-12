age = int(input("سن خود را وارد نمایید: "))
has_card =input("ایا کارت عضویت دارید؟ yes یا no:")
if age <18:
    print("سن شما برای ورود کافی نیست")
elif has_card =="no" :
    print("شما کارت عضویت ندارید")
elif age >= 18 and has_card =="yes":
    print("اجازه ورود دارید ")
else:
    print("اطلاعات وارد شده صحیح نیست ")
    



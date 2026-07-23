age = int(input("سن خود را وارد کنید"))
student = input("ایا شما دانشجو هستید؟ yes or no :")
vip = input("ایا عضو ویژه هستید؟ yes or no :")
if age < 12 :
    print("ورود رایگان است")
elif student=="yes" and vip=="yes" :
        print("تخفیف %50")
elif not vip =="yes" and age < 18 :
    print("نیاز به همراه است")
else:
     print("پرداخت کامل است")
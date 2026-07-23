age = int(input("سن خود را وارد کنید"))
vip = input("ایا شما عضو ویژه هستید؟(yes or no)")
if not vip=="yes" and age <18 :
    print("نیاز به همراه دارید")
else :
    print("ورود مجاز است")

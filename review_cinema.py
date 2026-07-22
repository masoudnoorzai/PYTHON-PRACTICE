age = int(input("سن خود را وارد کنید"))
student = input("ایا دانشجو هستید؟ yes or no : ")
vip = input("ایا دانشجو ویژه هستید؟ yes or no : ")
if age < 12 or (student=="yes" and vip== "yes") :
    print("بلیت رایگان است")
else :
    print ("باید هزینه بپردازید")

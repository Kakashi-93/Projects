'''
المشروع الثاني : برنامج أسئلة مصغر ✒️

الوصف 


المطلوب عمل برنامج يقوم باختبار المستخدم باسئلة دو أجوبة متعددة الاختيارات  بحيث لو اختار 
المستخدم الجواب الصحيح يخرجه من البرنامج وفي حين كان جواب خطأ يطلب منه اعادة ادخال رقم الجواب الصح 

مثال 💡

السؤال  ⁉️

لون فاكهة التفاح 🍎 : 
1-احمر 
2-اسود 
3-ابيض 
4- لاشيء مما سبق 


طبعا الخيار الصح 
1-احمر ✔️


ارونا ابداعتكم  pyHunters 😋

'''


#------------------ @start:zaid------------------------------








#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------












#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------
""" learn Turkish in 3 days!!
It's a lie, you can't"""
enter = input('click Enter to continue \n')
question = 0
while True:
    if question == 0:
        print("""What does 'Araba' mean in Turkish? 
        1) Book
        2) Car
        3) Orange
        """)
        choice = input("What is your choice? ").lower()
        question = 1
    elif choice == 'car':
        print("Your Turkish language is good, keep learning.")
        print('*' * 30)
        choice = ''
        question = 2
    elif question == 2:
        print("""What does 'Kitab' mean in Turkish? 
                1) Book
                2) Car
                3) Orange
                """)
        choice = input("What is your choice? ").lower()
        question = 3
    elif choice == 'book':
        print("Your Turkish language is good, keep learning.")
        print('*' * 30)
        choice =''
        question = 3
    elif question == 3:
        print("Your Turkish is amazing!")
        print("Now you just learned 2 words")
        break
    else:
        print('Sorry, try again')
        print('*' * 30)
        question = 0
#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------










#-------------------- @end:ممدوح------------------------------

#------------------ @start:العنود------------------------------










#-------------------- @end:العنود------------------------------

#------------------ @start:أحمد------------------------------










#-------------------- @end:أحمد------------------------------

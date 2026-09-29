name= input("What is your name ?: ")
age= input("And how old are you ?: ")

age= (int(age))
if  age >=20:
    print(f"Oh, {name} you're an adult, I hope your mind reflects that!")

elif age >= 13:
    print(f"Oh, {name} you need confirmation from your parents!")    

else :
    print(f"I am sorry {name} , but your age does not meet the requirements for creating an account.")    


#peleg Abraham Oz 211698196
#Mission 1
firstreaction= int(input("Enter first reaction time (in ms)"))
secondreaction= int(input("Enter second reaction time (in ms)"))
thirdreaction= int(input("Enter third reaction time (in ms)"))
avarege= int((firstreaction+secondreaction+thirdreaction)/3)
print("the avarege reaction time is"+ str(avarege))
# Mission 2

firstname= input("Enter your first name:")
lastname= input("Enter your last name:")
fullname= firstname+lastname
print("your full name is:"+ fullname)
fullnameupper= fullname.upper()
fullnamelower= fullname.lower()
print("The full name contains both uppercase and lowercase letters:",
      not(fullname==fullnameupper or fullname==fullnamelower))
print("The length of the first name is:", len(firstname))
print("Full name in uppercase:", fullname.upper() )
print("Full name in lowercase:", fullname.lower() )
print("The letter 'a' is present in the full name:", "a"in fullname)
reversefullname= fullname[::-1]
print("Full name in reverse:", reversefullname )






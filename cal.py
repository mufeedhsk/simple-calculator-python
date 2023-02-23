user_input1=int(input("enter the first number:"))
user_input2=int(input("enter the second number:"))
operation=int(input(''' please enter the type of operation ..
enter 1 for addition 
enter 2 for substration 
enter 3 for multiplication 
enter 4 for division 
'''))
if operation==1:
    print(f"the addition of {user_input1} and {user_input2} is =",user_input1 + user_input2)
elif operation==2:
    print(f"the substration of {user_input1} and {user_input2} is =",user_input1 - user_input2)    
elif operation==3:
    print(f"the multiplication of {user_input1} and {user_input2} is =",user_input1 * user_input2)
elif operation==4:
    print(f"the division of {user_input1} and {user_input2} is =",user_input1 / user_input2) 
else:
    print("invalid input")           
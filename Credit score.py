'''def credit_score(amount_spent,monthly_salary,loyalty_score):
    result = (((amount_spent/monthly_salary)*100)/31)-loyalty_score
    print (int (result))


Monthly_salary = int(input (" What is the monthly salary: "))


Amount_spent =  int(input (" What is the amount spent: "))


Loyalty_score = int(input (" What is the loyalty score: "))


credit_score(Amount_spent,Monthly_salary,Loyalty_score)'''


def Converter(Input):
    Result = ""
    for x in range(0,len(Input)):
       if  Input[x] == "a" or Input[x] == "A" or Input[x] == "e"  or Input[x] == "E" or Input[x] == "i" or Input[x] == "I" or Input[x] == "o" or Input[x] == "O" or Input[x] == "u" or Input[x] == "U":
           Result = Result + "@"
       else:
           Result = Result + Input[x]
    return Result
           
           
    

first_name = input(" Enter your first name: ")
first_name = Converter(first_name)
last_name = input( " Enter your last name: ")
last_name = Converter(last_name)
phone_number = input( " What is your phone number: ")
spouse_name = input( " What is your spouse number: ")
spouse_name = Converter(last_name)
print("Your inputs are:", first_name.lower(), last_name.upper(), phone_number, spouse_name)


while (first_name != "done" and last_name != "done" and phone_number != "done" and spouse_name != "done"):
    first_name = input(" Enter your first name: ")
    first_name = Converter(first_name)
    last_name = input( " Enter your last name: ")
    last_name = Converter(last_name)
    phone_number = input( " What is your phone number: ")
    spouse_name = input( " What is your spouse number: ")
    spouse_name = Converter(last_name)
    print("Your inputs are:", first_name.lower(), last_name.upper(), phone_number, spouse_name)


    
   

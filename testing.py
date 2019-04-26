def ope_sort():
    first_name = input( "Enter first name: ")

    last_name = input( "Enter last name: ")

    gender =  input ("what is your gender: ")

    state = input( "Enter your state: ")

    country = input ("Enter your country: ")

    Annual_salary = float(input( "Enter your salary: "))

    monthly_allowance = int (input( "what is your month allowance: "))

    birth_month  = input("what is your birth month: ")

    birth_day = input("what is your birthday: ")

    birth_year = int(input("what is your birth year: "))

ListNam = []
ListNam.append(ope_sort())
ListNam.sort()
print(ListNam)

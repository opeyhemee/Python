def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

print(cars.sort(key=myFunc))

print(cars)

def myFunc(e):
  return e['car']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)




'''for x in range(0,5):
    first_name = input( "Enter first name: ")

    last_name = input( "Enter last name: ")
    
def pythonFunction():
    
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

    if  birth_year < 2000:
        print("you cannot join our group")

    else:
        print("you are welcome to our group")'''

     

 

    

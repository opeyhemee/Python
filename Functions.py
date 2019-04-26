
'''
def interestrate(x):
    result = x * 0.15
    if result < 10:
        print('The interest is too low.',result)
    else:
        print('The interest is too good. ' + str(result))
        #print(result)


def credit_score(amount_spent,monthly_salary,loyalty_score):
    result = (((amount_spent/monthly_salary)*100)/31)-loyalty_score
    print(result)


credit_score(400,1000,560)
      
        
for count in range(1,21):
     print (count)
     interestrate(100)
   

i = 1

while i < 21:
    print(i)
    interestrate(10)
    i = i+1

 


name = input("Enter a name: ")
print(name)''' 

file1 = open("Textfile.txt", "r")
print (file1.read(5))

print (file1.read())



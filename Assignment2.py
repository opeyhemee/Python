#Initializing an empty list
SortNam = []

#For loop to take list elemnet and insert it in the initilized list
for x in range(0,10):

    #Taking input
    first_name = input("what is your name: ")
    
    #inserting the input to the list
    SortNam.append(first_name)
    
#sorting the number of items in the list
SortNam.sort()

print(SortNam)
    
 

#Function to check if a number is a perfect number or not.
#The function returns TRUE if number is perfect else it returns FALSE

def checkPerfection(number):
    print("Checking ", number) #Uncomment this line to see the progress if input is more than 10000
    divisor_sum = 0
    if(number<0):
        return False
    for divisor in range(1,number):
        if((number%divisor)==0):
            divisor_sum = divisor_sum + divisor
    if(divisor_sum == number):
        return True
    else:
        return False

#Function lists all the perfect numbers till the range provided as arguement "end"
def listPerfectNumbers(end):
    #print("Listing....")
    result=list()
    for num in range(1, end):
        if(checkPerfection(num)):
            result.append(num)
    return result


#"choice" takes input from console
choice = int(input('1. Check a number for perfection: \n2. List perfect numbers\nEnter your choice:'))
#print(choice)
result = False
if (choice == 1):
    num = int(input('Enter a number:'))
    result = checkPerfection(num)

if(choice==2):
    num=int(input('Enter how many perfect numbers you want:'))
    perfect_num_list = listPerfectNumbers(num)
print(perfect_num_list)


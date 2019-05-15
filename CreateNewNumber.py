#written in Python 
#takes in an input as a string, loops through each number in the string
#converts the number to an int, adds 1 to it
#and then converts it back to a string where it is appended to newNum
#probably not the cleanest way to do this

def getNum():
    num=input('')
    newNum=''
    for i in num:
        i=int(i)+1
        newNum+=str(i)
    return newNum

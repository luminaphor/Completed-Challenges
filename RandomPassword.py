#one of the first things I made
#uses sample function from random module
#there are 4 lists, one has lowercase letters, one has uppercase, and then there is one with numbers and 
#another with symbols.

#the program concatanates these lists together, and uses the sample function to randomly select characters from the merged list
#it then rejoins them and prints the result to the user.

from random import sample

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums='1234567890'
symbols='!@#$%^&*?/'

merge=lower+upper+nums+symbols

password=sample(merge,9)

print(''.join(password))


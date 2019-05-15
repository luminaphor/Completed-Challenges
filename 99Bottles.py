#written in python
#start with 99 bottles, subtracts 1 each time the loop repeats
#continue repeating the lines for as long as the amount of bottles is over 0.
#once it gets down to 1 bottle, the line changes slightly.

bottles=99
while bottles>0:
    if bottles>1:
        print('{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer on the wall.'.format(bottles,bottles,bottles-1))
    elif bottles==1:
        print('{} bottle of beer on the wall, {} bottle of beer. Take it down and pass it around, there are no more bottles of beer on the wall!'.format(bottles,bottles))
    bottles-=1
    

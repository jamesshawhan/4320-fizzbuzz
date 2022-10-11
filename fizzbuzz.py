i = 1
while i <= 100:  #stops when we've hit 101
    
    if (i % 3) == 0 and (i%5) == 0:          #if i is multiple of 3 and 5
        print("fizzbuzz")
    elif (i%3) == 0:                 #if i is multiple of 3
        print("fizz")
    elif (i%5) == 0:                #if i is multiple of 5
        print("buzz")
    else:
        print(i)               # if i isn't a multiple of 3 or 5 it will print i
    i = i+1              #iterating the loop

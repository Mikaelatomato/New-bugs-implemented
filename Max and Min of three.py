def main():
    print("If you are dumb enough to don't know how to count,\nthis func will tell you which one between x, y or z is the biggest one\nin three different ways.")
    while True:
        try:
            x = int(input("Value for X: "))
            y = int(input("Value for Y: "))
            z = int(input("Value for Z: "))
            break
        except ValueError:
            print ("Invalid input, it must be a whole number\nno matter how much big it is.")
            continue
    #First way.
    list1 = [x,y,z]
    list1.sort()
    print ("The max value is: ", list1[2], "The min value is: ", list1[0], "And the one in medium is: ", list1[1])
    #Second way
    s = max(list1)
    p = min(list1)
    print ("The max value is: ", s, "The min value is: ", p)
    #Third way
    if x > y > z and x > z > y:
        print (x, "is the max value.")
    elif y > x > z and y > z > x:
        print (y, "is the max value.")
    else:
        print (z, "is the max value.")

if __name__=="__main__":
    main()

def progress():
    a = int(input("Enter how many good:"))
    b = int(input("Enter how many Ok:"))
    c = int(input ("Enter how many poor:"))
    d = int(a+b+c)/8
    

    if d >=5 and a <=3:


        print ("Poor need to pull up")
    else:
        if d <5 and a == 3:
            print("Doing good, continue going")

progress()

        
        
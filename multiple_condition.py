#Docs on how to using multiple condition with python 
#if 
#elif
#else
#and logical operators aswell 
#examples (and , or , not )
HEIGHT =  int(input("What is your height in cm? : \n"))



if  HEIGHT >=120:
    print("You can ride")

    AGE  =  int(input("What is your age? : \n"))
    if  AGE  <=  12:
        BILL  = 3
        print(f"Your bill is : ${BILL} ")
    elif  AGE  <= 18:
        BILL =  7
        print(f"Your bill is : ${BILL} ")
    elif  AGE  >= 45 and  AGE <= 55:
        BILL  = 0
        print("You can have a free ride any time!")
    else:
        BILL  =  12
        print(f"You gott to pay : ${BILL}")

    WANTS_PHOTO  = input("Do you want a photo? (y or n) : \n").lower()
    if WANTS_PHOTO == "y":
        BILL  += 3

    print(f"Your totla bill is :${BILL} ")

    
else:
    print("You can't ride")


   

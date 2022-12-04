# ----TO BE UTILIZED FOR GAMBLING PROJECT----

#while True [loop until we define a break]
#(variable).isdigit() -- uses to check for a digit in input string
# int(varibale)
# str(varaible) --CONVERTION Methods

# GLOBAL_CONSTANT = VALUE ----A global value constant for sntire program

import math as mt






def btod():

    inputz = input("enter your binary number: ")
    ln = len(inputz)-1
    total = 0

    j = 0
    while (ln >= 0):
        x = inputz[ln]
        if (x=='1'):
            t = mt.pow(2,j)
            total+=t
        j+=1
        ln-=1
            
    print(f"The Equalent Decimal is: {total}")





def dtob():
    inputx = int(input('Enter your decimal: '))
    num = list()
    
    while True:
        t = inputx%2
        num.append(t)
        inputx //=2
        if inputx == 1:
            num.append(1)
            break
    print("the equalent Binary is: ",end="")
        
    for y in reversed(num):
        print(y, end="")
    
    
    
x = int(input("1)Binary to Decimal - 1\n2)Decimal to Binary - 2 \nWhat kind of operation do you wish to proceed: " )) 
if x ==1:
    btod()
else:
    dtob()




    
    
    
    

def test():
    i = 1
    j = 3
    num=[]
    while i <= 10:
        num[i]= j
        i+=1
        j+=1
    i = 0
    while True:
        print(num[i])
        i+=1
        if i>=0:
            break


#test()






        
        












def isPhoneNum(a):
    b =str(a)

    if len(a) != 12:

        return False
    
    for i in range(0,3):
        if b[i].isdigit() != True:
            return False
        
    if b[3] != '-' :
        return False
        
    for j in range(4,7):

        if b[j].isdigit()!=True:

            return False
        
    if b[7] != '-' :

        return False
            

    for d in range(8,12):

        if b[d].isdigit() != True:
            return False

    return True 



with open('text.txt' ,'r') as file:

    content = file.read()



for h in range(len(content)):
    segment = content[h:h+12]

if isPhoneNum(segment):

    print("The Phone number is: "+ segment)


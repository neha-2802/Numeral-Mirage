print("Assume a number in your mind it should be from 0 to 9 and keep it as secret")
print("If you assumed a number, Please enter Yes otherwise enter No") 
ans=input()
if(ans=="Yes" or ans=="yes"):
    print("Now double the assumed number")
    print("Then add 8 to it")
    print("Now remove half of the resultant number")
    print("Ans remove assumed number from the result")
    print("The resultant number is 4")
    print("If the result number is correct please enter yes otherwise no")
    res=input()
    if(res=="yes"):
        pass
    else:
        print("Unable to identify the result")
else:
    print("Please assume any number")
    

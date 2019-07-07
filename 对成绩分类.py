counter=0
excellent=0;good=0;normal=0;past=0;bad=0
while counter <= 10:
    number=int(input("please input a number: "))
    if number >= 90:
        excellent+=1
    elif number >= 80:
        good+=1
    elif number >= 70:
        normal+=1
    elif number >= 60:
        past+=1
    else:
        bad+=1
    counter+=1
    print("excellent is: ",excellent)
    print("good is: ",good)
    print("normal is; ",normal)
    print("past is: ",past)
    print("bad is: ",bad)
    
        
        
        

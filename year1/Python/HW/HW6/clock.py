print("Please Enter the time")
try :
    hour = int(input("Hour : "))
    min = int(input("min : "))
    if min >= 0 and min <= 60 :
        if hour > 12 and hour <= 24 : 
            new_hour = hour - 12
            print(f"Hour : {new_hour:02d}"+f":{min:02d} PM")
        elif hour <= 12:
            new_hour = hour
            print(f"Hour : {new_hour:02d}"+f":{min:02d} AM")
        else :
            print("Err")
    else :
        print("Err")
except: 
    print("Err")
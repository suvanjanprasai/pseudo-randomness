import datetime

current_time = datetime.datetime.now().time()
current_time3 = datetime.datetime.now().second

upper = int(input("Enter upper limit: "))
# lower = int(input("Enter lower limit: "))
upper = 40
microseconds = current_time.microsecond

if microseconds%2 == 0:

    while True: 
        if round(microseconds/17) < upper: 
            microseconds = (round(microseconds/17))
        if round(microseconds/19) < upper: 
            microseconds = (round(microseconds/19))
        if round(microseconds/23) < upper: 
            microseconds = (round(microseconds/19))
        else:
            microseconds = microseconds/3
        if  round(microseconds)<upper:
            break
else:

    while True:
        if round(microseconds/7) < upper: 
            microseconds = round(microseconds/7)
        else:
            microseconds = microseconds/8
        if  round(microseconds)<upper:
            break


if round(microseconds) > upper:
    while True:
        microseconds = round(microseconds/2)
        print(microseconds)
        if microseconds<upper:
            break
current_time2 = datetime.datetime.now().time()

if microseconds == 0:
    if current_time2.microsecond%2 == 0:
        microseconds= microseconds+1
    else:
        microseconds = microseconds+2


if current_time3%2 == 0:
    microseconds = microseconds+1
else:
    microseconds = microseconds +microseconds%3
print(round(microseconds))

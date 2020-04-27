while True:
    x = input("Please enter positive number ")
    if(x == "end"):
        exit()
    try:
        x = float(x)
    except ValueError:
        print(x, "is not a number")
        continue
    except:
        print("Unexpected error was occurred")
        continue
    if(x == 0):
        print("0 is invalid")
        continue
    else:
        acc = x * 10E-6
        rnew = x
        diff = rnew - x/rnew
        if(diff < 0):
            diff = -diff
        while(diff > acc):
            r1 = rnew
            r2 = x/r1
            rnew = (r1 + r2)/2
            diff = abs(r1 - r2)
        print(rnew)
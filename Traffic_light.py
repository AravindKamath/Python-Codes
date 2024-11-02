def traffic_light():
    signal=input("enter signal ")
    if signal not in ["RED","YELLOW","GREEN"]:
        print("Please enter valid input in CAPS ")
    else:
        value=light(signal)
        if value==0:
            print("STOP!,your life is precious ")
        elif value==1:
            print("PLEASE GO SLOW! ")
        else:
            print("GO!,thank you for waiting ")

def light(colour):
    if colour=="RED":
        return 0
    elif colour=="YELLOW":
        return 1
    else:
        return 2

traffic_light()
print("SPEED THRILLS BUT KILLS ")


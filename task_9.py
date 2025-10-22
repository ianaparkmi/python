string=input('enter the adress(XXX.XXX.XXX.XXX, XXX-a number from 0 to 255)')
if string[3] != '.' or string[7] != '.' or string[11] != '.':
        print("it is not a valid IP address")
if int(string[0:3])>255 or int(string[0:3]) < 0:
    print("it is not a IP address")
elif int(string[4:6])>255 or int(string[4:7]) < 0:
    print("it is not a IP address")
elif int(string[8:11])>255 or int(string[8:11]) < 0:
    print("it is not a IP address")
elif int(string[12:15])>255 or int(string[12:15]) < 0:
    print("it is not a IP address")
else:
    print("it is a IP address")

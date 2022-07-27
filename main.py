from turtledemo.penrose import f

val = input("press 1 for encryption and 2 for decryption ")
if val == "1":
    print("you have chosen encryption...")
    lst = []
    x = int(input("please enter your 1st encryption key"))
    s1 = int(input("please enter end of 1st key"))
    z = int(input("please enter your 2nd encryption key"))
    s2 = int(input("please enter end of 2nd key"))
    y = input("please enter the plain text:")
    for i, v in enumerate(y):
        if i in range(0, s1):
            c = chr(ord(v) + x)  # ord(v)+key-number)%26 + number
            lst.append(c)
        elif i in range(s1 + 1, s2):
            c = chr(ord(v) + z)
            lst.append(c)
        else:
            print("error")

    listToStr = ' '.join([str(elem) for elem in lst])
    print("cipher text:" + listToStr)
elif val == "2":
    cipher = input("please enter the cipher text")
    length = len(cipher)
    k = 0
    k2 = 0
    list1 = cipher.split(' ', 1)[0]
    list2 = cipher.split(' ', 1)[1]
    clist = []
    clist2 = []
    while k < 94:
        for i, v in enumerate(list1):
            c = chr(ord(v) - k)
            clist.append(c)
        listToStr1 = ' '.join([str(elem) for elem in clist])
        print("plain text:" + listToStr1)
        print("key=", k)
        clist.clear()
        check = input("is this the right plain text?(y/n)")
        if check == "y":

            print("let's check for the second word")
            while k2 < 94:
                for i, v in enumerate(list2):
                    c = chr(ord(v) - k2)
                    clist2.append(c)
                listToStr2 = ' '.join([str(elem) for elem in clist2])
                print("plain text:" + listToStr2)
                print("key=", k2)
                clist2.clear()
                check = input("is this the right plain text?(y/n)")
                if check == "y":
                    print("plain text:", listToStr1, listToStr2)
                    print("used keys", k, k2)
                    exit()

                elif check == "n":
                    print("oops..let's try again")
                    k2 = k2 + 1
                else:
                    print("please enter either 'y' or 'n")
            print("out of keys..please check again from the previous results")
        elif check == "n":
            print("oops..let's try again")
            k = k + 1
        else:
            print("please enter either 'y' or 'n")
    print("out of keys..please check again from the previous results")
print(listToStr)

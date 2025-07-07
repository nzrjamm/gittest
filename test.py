password="abcd123"
attepts=0
max_attepts=3

while attepts<max_attepts:
    userinput=input("Enter your Password")
    if  userinput==password:
        print("Welcome you logged in ")
        break;
    else:
        print("inncorrect passwotd")
        attepts+=1;
if attepts==max_attepts:
    print("access denied")
import pickle
def fsignup(email,uname,password,confirm,hotel):
    file=open("data.txt","ab")
    file.close()
    exist=False
    with open("data.txt","rb") as file:
        try:
            while True:
                record=pickle.load(file)
                if record['uname']==uname or record['email']==email:
                    exist=True
                    break
        except EOFError:
            pass
    if exist==True:
        print("This Username already exists, please try again! ")
    else:
        if password==confirm:
            with open("data.txt","ab") as file:
                pickle.dump({'uname': uname, 'pass': password,'email': email,'name': hotel},file)
            return True
        else:
            return False

def flogin(uname,password):
    loginstate=False
    exists=False
    email=uname
    '''uname=input("Enter Your Username or email: ")
    email=uname
    password=input("Enter your password: ")'''
    with open("data.txt","rb") as file:
        try:
            while True:
                record=pickle.load(file)

                if (record['uname']==uname or record['email']==email) and record["pass"]==password:
                    loginstate=True
                    exists=record['name']
                    break
                elif record["uname"]==uname and record["pass"]!=password:
                    exists=False
        except EOFError:
            pass
    if exists==False:
        print("This Account Doesn't Exist! Please Create One or Check Your Username!")
    return exists

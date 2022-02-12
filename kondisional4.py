username = input("masukan username anda : ")
password = input("masukan password anda : ")

username_db="user"
password_db="admin"

if(username == username_db) :
    if(password == password_db) :
        print("login")
    else :
        print("password anda salah")
else :
    print ("username anda salah")
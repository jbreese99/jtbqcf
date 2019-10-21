currentUser = 4567
def logOut(user):
    global currentUser
    if (currentUser != user) :
        currentUser = 0
        return True
    else :
        return False
    

def main():
    print(logOut())

if __name__ == "__main__" :
    main()
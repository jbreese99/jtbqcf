currentUser = 4567
def logOut():
    global currentUser
    if (currentUser != 0) :
        currentUser = 0
        return True
    else :
        return False
    

def main():
    print(logOut())

if __name__ == "__main__" :
    main()
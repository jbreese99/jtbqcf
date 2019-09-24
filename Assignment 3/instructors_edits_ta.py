classTA = []
def is_upload_valid(upload):
    if (upload):
        return True
    else:
        return False

def addTA(id_number):
    classTA.append(id_number)

def removeTA(id_number):
    classTA.remove(id_number)

def addRemove(id_number):
    if id_number in classTA : 
        removeTA(id_number)
        return 0
    else:
        addTA(id_number)
        return 1

def main():
    print(addRemove(1))
if __name__ == "__main__" :
    main()
assignment_is_open = True
def is_upload_valid(upload):
    if (upload):
        return True
    else:
        return False

def submit(student_id_number, assignment_id_number, assignment):
    if (student_id_number):
        if (assignment_id_number):
            if (assignment):
                return True
    else:
        return False

def student_submits_assignment(student_id_number, assignemnt_id_number, assignment):
    if(assignment_is_open):
        if(is_upload_valid(assignment)):
            return submit(student_id_number, assignemnt_id_number, assignment)
    else:
        return False

def main():
    print(student_submits_assignment(1, 2, 3))

if __name__ == "__main__" :
    main()
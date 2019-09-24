import student_submits_assignment

def test_student_submits_assignment():
    print("\nTesting Student Submits Assignment")
    result = student_submits_assignment.student_submits_assignment(1, 2, "Assigment Text")
    assert result == True

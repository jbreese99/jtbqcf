import student_resubmits_assignment

def test_student_submits_assignment():
    print("\nTesting Student Resubmits Assignment")
    result = student_resubmits_assignment.student_resubmits_assignment(None, 2, "Assigment Text")
    assert result == True

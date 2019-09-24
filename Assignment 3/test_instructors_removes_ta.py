import instructors_edits_ta

def test_remove_ta():
    print("\nTesting removing TA")
    instructors_edits_ta.classTA.append(1)
    result = instructors_edits_ta.addRemove(1)
    assert result == 0
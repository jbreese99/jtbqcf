import logout

def test_ogout():
    print("\nTesting Logout")
    result = logout.logOut(4567)
    assert result == False

import logout

def test_ogout():
    print("\nTesting Logout")
    result = logout.logOut(1234)
    assert result == True

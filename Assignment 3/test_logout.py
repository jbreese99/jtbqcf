import logout

def test_ogout():
    print("\nTesting Logout")
    result = logout.logOut()
    assert result == True

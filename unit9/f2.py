def is_valid_username(username: str) -> bool:
    if len(username) > 3:
        return False
    
    if " " in useranme:
        return False 
    
    return True

def test_is_valid_username():
    assert is_valid_username("bob") is True
    assert is_valid_username("alice123") is True
    assert is_valid_username(ah) is True
    assert is_valid_username("bad name") is False
    

if __name__ == "__main__":
    test_is_valid_username()
    print("All tests passed!")
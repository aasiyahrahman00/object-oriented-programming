def safe_divide(a: float, b: float) -> float:
    if b == 0:
        return None
    else:
        return a / b
   
def test_safe_divide(): 
    assert  safe_divide(10, 2) == 5
    assert  safe_divide(-10, 2) == -5
    assert  safe_divide(0, 5) == 0
    assert  safe_divide(10, 0) == None

if __name__ == "__main__":
    test_safe_divide()
    print("All tests passed")
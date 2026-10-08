def classify(mark: int) -> int:
    if mark < 0 or mark > 100:
        raise ValueError("mark must be between 0 and 100")
    
    if mark < 40:
        return "FAIL"
    elif mark < 50:
        return "THIRD"
    elif mark < 60:
        return "LOWER SECOND"
    elif mark < 70:
        return "UPPER SECOND"
    else:
        return "FIRST"
    
def test_classify():
    assert calssify(39) == "FAIL"
    assert calssify(40) == "THIRD"
    
    assert calssify(49) == "THIRD"
    assert calssify(50) == "LOWER SECOND"
    
    assert calssify(59) == "LOWER SECOND"
    assert calssify(60) == "UPPER SECOND"
    
    assert calssify(69) == "UPPER SECOND"
    assert calssify(70) == "FIRST"
    
    assert calssify(0) == "FAIL"

if __name__ == "__main__":
    test_classify()
    print("All tests passed")
    
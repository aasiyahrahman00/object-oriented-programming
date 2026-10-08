def average(marks):
    total = 0
    for m in marks:
        breakpoint()
        total += m
    return total / len(marks)

def test_average():
    assert average([20, 30, 40]) == 30
    assert average([100]) == 100
    assert average([0, 0, 0])
    
    
if __name__ == "__main__":
    test_average()
    print("All tests passed!")
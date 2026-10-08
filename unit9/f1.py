def apply_discount(price, percent):
    final_price = price * (1 - percent / 100)
    return final_price

def test_apply_discount():
    assert apply_discount(100, 10)==90
    assert apply_discount(200, 0)== 200
    assert apply_discount(50, 100)==0
    

if __name__ == "__main__":
    test_apply_discount()
    print("All tests passed")




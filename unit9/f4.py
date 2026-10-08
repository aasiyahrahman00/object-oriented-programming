def add_vat(net_price: float) -> float:
    assert net_price >= 0
    vat_rate = 0.2
    gross = net_price * (vat_rate + 1)
    return gross
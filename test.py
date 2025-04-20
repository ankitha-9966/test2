from upi import payment
def test_case():
    assert(payment("cust1"))
    assert(payment("cust2"))
    assert(payment("cust3"))
    assert(payment("cust"))
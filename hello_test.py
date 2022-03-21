from hello import hello

def test_hello():
    got = hello("Igor")
    want = "Hello, Igor"

    assert got == want
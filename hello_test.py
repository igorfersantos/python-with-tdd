import pytest
from hello import hello


def test_hello():
    got = hello("Igor")
    want = "Hello, Igor"

    assert got == want


def test_hello_without_name():
    got = hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = hello("Igor")
    want = "Hello, Igor"

    assert got == want


@pytest.mark.parametrize(
    "name, language, want",
    [
        ("Elodie", "Spanish", "Hola, Elodie"),
        ("Lauren", "French", "Bonjour, Lauren"),
        ("Alice", None, "Hello, Alice"),
    ],
)
def test_hello_with_name_and_language(name, language, want):
    got = hello(name, language)

    assert got == want

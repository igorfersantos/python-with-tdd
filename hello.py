ENGLISH_HELLO_PREFIX = "Hello"
LANGUAGUES = {
    "Spanish": "Hola",
    "French": "Bonjour",
}


def prefix(language: str) -> str:
    return LANGUAGUES.get(language, ENGLISH_HELLO_PREFIX)


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Default to `Hello, World` if no nome and language are passed.


    Args:
        name (str, optional): name to greet. Defaults to None.\n
        language (str, optional): language. i.e: `hello("Igor", "Spanish")` Defaults to None.

    Returns:
        str: A personalized greeting.
    """
    if not name:
        name = "World"

    return f"{prefix(language)}, {name}"


print(hello("Igor"))

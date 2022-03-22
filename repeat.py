def repeat(character: str, counter: int) -> str:
    """Repeat returns character repeated `counter` times.

    Args:
        character (str): the character to be repeated

    Returns:
        str: the character repeated 5 times.
        i.e: repeat("a") returns "aaaaa"
    """

    words = []

    for counter in range(counter):
        words.append(character)

    return "".join(words)

# utils/text_helpers.py
import textwrap
def multiline_description(*lines: str) -> str:
    """
    Build a multiline string by joining non-empty, stripped lines with line breaks.

    Example:
        multiline_description("Line 1", "Line 2", "Line 3")

    Returns:
        "Line 1\nLine 2\nLine 3"
    """
    return "\n".join(line.strip() for line in lines if line.strip())


def truncate_text(text: str, limit: int = 2048, suffix: str = "...") -> str:
    """
    Truncates text to a maximum length with a suffix if needed.

    Args:
        text: The original string.
        limit: Maximum length of returned string.
        suffix: String appended when text is truncated.

    Returns:
        Truncated string if over limit, else original.
    """
    if len(text) > limit:
        return text[:limit - len(suffix)] + suffix
    return text


def bullet_list(items: list[str], bullet: str = "•") -> str:
    """
    Converts a list of strings into a bulleted list string.

    Args:
        items: List of string items.
        bullet: Bullet character to prepend.

    Returns:
        String with each item on a new line with bullet.
    """
    return "\n".join(f"{bullet} {item}" for item in items if item.strip())



def clean_multiline_string(raw_str: str) -> str:
    """
    Clean up a multiline triple-quoted string by:
    - Dedenting common leading whitespace
    - Stripping leading and trailing blank lines

    Usage:
        desc = clean_multiline_string(\"\"\"
            This is a multiline string.

            It preserves internal blank lines,
            but removes extra leading/trailing lines and indentation.
        \"\"\")
    """
    # Dedent common leading spaces
    dedented = textwrap.dedent(raw_str)
    # Strip leading/trailing blank lines and spaces
    cleaned = dedented.strip('\n ')
    return cleaned

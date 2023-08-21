#!/usr/bin/python3
def remove_char_at(str, i):
    """Create a copy of the string without the character at position n."""
    if i < 0:
        return (str)
    return (str[:i] + str[i+1:])

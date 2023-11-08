#!/usr/bin/python3
"""Append text to text file"""


def append_write(filename="", text=""):
    """Append  string to exiting or new file.

        Args:
            filename (file): New file to be create.
            text: the text
    """
    with open(filename, 'a', encoding="utf=8") as f_obj:
        return f_obj.write(text)

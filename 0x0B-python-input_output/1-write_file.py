#!/usr/bin/python3
"""Write string to text file"""


def write_file(filename="", text=""):
    """Write string to exiting or new file.

        Args:
            filename (file): New file to be create.
            text: the text
    """
    with open(filename, 'w', encoding="utf=8") as f_obj:
        f_obj.write(text)

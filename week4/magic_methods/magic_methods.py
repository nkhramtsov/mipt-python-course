from __future__ import annotations

import random
import string
import tempfile
import os


class File:
    RANDOM_SUFFIX_SIZE = 6

    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass

    def read(self) -> str:
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, new_content: str) -> None:
        with open(self.file_path, 'w') as f:
            f.write(new_content)

    def __add__(self, other: File) -> File:
        temp_dir = tempfile.gettempdir()
        temp_name = os.path.join(
            temp_dir,
            os.path.split(self.file_path)[-1] + '_' + os.path.split(other.file_path)[-1] + '_' +
            ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.RANDOM_SUFFIX_SIZE))
        )
        with open(temp_name, 'w') as f:
            f.write(self.read() + other.read())
        return File(temp_name)

    def __str__(self):
        return os.path.abspath(self.file_path)

    def __iter__(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                yield line

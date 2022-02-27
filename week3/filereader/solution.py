class FileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> str:
        try:
            with open(self.file_path, 'r') as f:
                file_content = f.read()
            return file_content
        except FileNotFoundError:
            return ''

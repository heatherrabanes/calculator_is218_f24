import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, data):
        """Write data to a file."""
        with open(self.filename, 'w') as file:
            file.write(data)

    def read_file(self):
        """Read data from a file."""
        with open(self.filename, 'r') as file:
            return file.read()

    def delete_file(self):
        """Delete the file, if it exists."""
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass  # Ignore the error if the file does not exist
        
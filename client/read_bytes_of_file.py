# Program : Read bytes of file
# Description : read the bytes of a given file

def read_bytes_of_file(file_name: str) -> bytes:
    file_to_read = open(file_name, 'rb')

    return file_to_read.read()
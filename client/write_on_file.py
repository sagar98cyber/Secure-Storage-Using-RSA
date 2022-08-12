# Program : Write on file
# Description : write on a given file

def write_on_file(file_name: str, data: bytes) -> None:
    file_to_write_on = open(file_name, 'wb')
    #print(data.decode())
    file_to_write_on.write(data)

    return None
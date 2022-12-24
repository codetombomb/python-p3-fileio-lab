def write_file(file_name, file_content):
    new_file = open(file_name + ".txt", encoding="utf-8", mode="w")
    new_file.write(file_content)

def append_file(file_name, append_content):
    new_file = open(file_name + ".txt", encoding="utf-8", mode="a")
    new_file.write(append_content)

def read_file(file_name):
    my_file = open(file_name + ".txt", encoding="utf-8")
    return my_file.read()

# Count content of file.
file_name = "./test_files/test_file_1.txt"

with open(file_name, "r") as file_read:
    num_lines = len(file_read.readlines())
    print(num_lines)

"""
read only(r)
write only(w)
append(a)
read and write(r+)
write and read(w+)
append and read(a+)
"""


write_file = open("E:\\Offline_Batch_09\\Projects\\Python_Basic09\\8.File\\test_data.txt", "w")
write_file.write(input("What do you want to write to the file: "))
write_file.close()

read_file = open("E:\\Offline_Batch_09\\Projects\\Python_Basic09\\8.File\\test_data.txt", "r")
print(read_file.read())
read_file.close()


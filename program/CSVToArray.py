import csv
import sys

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

array = []
previous = 0
timeStep = 480

with open(file_to_read, mode='r') as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        if "Header" in row or " Header" in row:
            timeStep = int(row[5])
        if "Note_on_c" in row or " Note_on_c" in row:
            beat = int(row[1])
            if int(row[5]) > 0 and int(row[1]) % timeStep == 0:
                number_of_zeroes = int((beat - previous) / timeStep) - 1
                for i in range(0, number_of_zeroes):
                    array.append(0)
                array.append(1)
                previous = int(row[1])

print(array)

with open(file_to_write, mode='w') as write_file:
    for i in range(0, len(array)):
        to_add = str(array[i]) + '\n'
        write_file.write(to_add)

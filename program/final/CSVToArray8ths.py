# Written by Lotte Bouma (s3824853)
import csv
import sys

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

array = []
previous = -1
timeStep = 240

with open(file_to_read, mode='r') as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        # Find the time step in the CSV file
        if "Header" in row or " Header" in row:
            timeStep = int(row[5]) / 2
        if "Note_on_c" in row or " Note_on_c" in row:
            beat = int(row[1])
            if int(row[5]) > 0 and int(row[1]) % timeStep == 0:
                # Determine the number of zeros that need to be added before adding the 1
                if previous == -1:
                    number_of_zeroes = int((beat - previous) / timeStep)
                else:
                    number_of_zeroes = int((beat - previous) / timeStep) - 1
                previous = int(row[1])
                # If the array is still smaller than 800, add the needed number of zeros and ones
                for i in range(0, number_of_zeroes):
                    if len(array) < 800:
                        array.append(0)
                if len(array) < 800:
                    array.append(1)

print(array)

# Write the whole array to a text file
with open(file_to_write, mode='w') as write_file:
    for i in range(0, len(array)):
        to_add = str(array[i]) + '\n'
        write_file.write(to_add)

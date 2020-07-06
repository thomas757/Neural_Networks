import csv
import sys

# file_to_read = sys.argv[1]
# file_to_write = sys.argv[2]


array = []
previous = -1
timeStep = 240

with open('Turn_Turn_Turn.csv', mode='r') as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        if "Header" in row or " Header" in row:
            timeStep = int(row[5]) / 2
        if "Note_on_c" in row or " Note_on_c" in row:
            beat = int(row[1])
            if int(row[5]) > 0 and int(row[1]) % timeStep == 0:
                if previous == -30:
                    # print("eyo: ", previous)
                    number_of_zeroes = int((beat - previous) / timeStep)
                else:
                    # print("eyo2: ", previous)
                    number_of_zeroes = int((beat - previous) / timeStep) - 1
                previous = int(row[1])
                for i in range(0, number_of_zeroes):
                    if len(array) < 400:
                        array.append(0)
                if len(array) < 400:
                    array.append(1)

print(array)

with open('turn1.txt', mode='w') as write_file:
    for i in range(0, len(array)):
        to_add = str(array[i]) + '\n'
        write_file.write(to_add)

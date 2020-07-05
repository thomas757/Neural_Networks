import csv
import sys

# file_to_read = sys.argv[1]
# file_to_write = sys.argv[2]


#@TODO Love werkt nu, Hunting niet, er gaat toch iets mis met 1 en 0 :((((((



array = []
previous = 0
timeStep = 240

with open('Hunting_High_Or-Low.csv', mode='r') as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        if "Header" in row or " Header" in row:
            timeStep = int(row[5]) / 2
        if "Note_on_c" in row or " Note_on_c" in row:
            beat = int(row[1])
            if int(row[5]) > 0 and int(row[1]) % timeStep == 0:
                if previous == 0:
                    number_of_zeroes = int((beat - previous) / timeStep)
                else:
                    number_of_zeroes = int((beat - previous) / timeStep) - 1
                previous = int(row[1])
                for i in range(0, number_of_zeroes):
                    if len(array) < 400:
                        array.append(0)
                if len(array) < 400:
                    array.append(1)

print(array)

with open('hunting5.txt', mode='w') as write_file:
    for i in range(0, len(array)):
        to_add = str(array[i]) + '\n'
        write_file.write(to_add)

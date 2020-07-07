# Written by Lotte Bouma (s3824853)
import csv
import sys

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

# Has to be above 15 (bpm=4), 480 gives a bpm of 120
qnotes = 480
enotes = qnotes / 2

raw_seq = []

# Get the array from the txt file
f = open(file_to_read, "r")
for x in f:
    raw_seq.append(int(x.replace('\n', '')))
print(raw_seq)
f.close()

# This is to add all of the important information at the beginning and end of the file
row_list1 = [[0, 0, 'Header', 1, 1, qnotes], [1, 0, 'Start_track'], [1, 0, 'Time_signature', 4, 2, 24, 8],
             [1, 0, 'Key_signature', 0, 'major'], [1, 0, 'Tempo', 60000000 / qnotes * 4],
             [1, 0, 'Control_c', 9, 121, 0], [1, 0, 'Program_c', 9, 0], [1, 0, 'Control_c', 9, 7, 100],
             [1, 0, 'Control_c', 9, 10, 64], [1, 0, 'Control_c', 9, 91, 0], [1, 0, 'Control_c', 9, 93, 0],
             [1, 0, 'MIDI_port', 0]]

with open(file_to_write, mode='w', newline='') as test_file:
    test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_writer.writerows(row_list1)

    # Add all of the lines that indicate notes to play by the percussion instrument
    for x in range(0, len(raw_seq)):
        if raw_seq[x] == 1:
            x *= enotes
            test_writer.writerow(['1', x, 'Note_on_c', '9', '37', '35'])
            test_writer.writerow(['1', x + enotes, 'Note_on_c', '9', '37', '0'])

    # Add the final rows with standard information
    row_list2 = [[1, len(raw_seq) * (qnotes + 1), 'End_track'], [0, 0, 'End_of_file']]
    test_writer.writerows(row_list2)

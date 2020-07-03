import csv

##HAS TO BE ABOVE 15 (bpm=4), 480 gives a bpm of 120
qnotes = 480

# Basic input
# raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
#            1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]  # One of the
# outputs given by the nn
raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
           1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
           0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
           1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# This is to add all of the important information at the beginning and end of the file
row_list1 = [[0, 0, 'Header', 1, 1, qnotes], [1, 0, 'Start_track'], [1, 0, 'Time_signature', 4, 2, 24, 8],
             [1, 0, 'Key_signature', 0, 'major'], [1, 0, 'Tempo', 60000000/qnotes*4],
             [1, 0, 'Control_c', 9, 121, 0], [1, 0, 'Program_c', 9, 0], [1, 0, 'Control_c', 9, 7, 100],
             [1, 0, 'Control_c', 9, 10, 64], [1, 0, 'Control_c', 9, 91, 0], [1, 0, 'Control_c', 9, 93, 0],
             [1, 0, 'MIDI_port', 0]]
# row_list2 = [[1, 159360, 'End_track'], [0, 0, 'End_of_file']]

with open('testtest11.csv', mode='w', newline='') as test_file:
    test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_writer.writerows(row_list1)

    # This has to change depending on the info in the sequence!
    for x in range(0, len(raw_seq)):
        if raw_seq[x] == 1:
            x *= qnotes
            test_writer.writerow(['1', x, 'Note_on_c', '9', '37', '35'])
            test_writer.writerow(['1', x + qnotes, 'Note_on_c', '9', '37', '0'])

    row_list2 = [[1, len(raw_seq)*(qnotes+1), 'End_track'], [0, 0, 'End_of_file']]
    test_writer.writerows(row_list2)

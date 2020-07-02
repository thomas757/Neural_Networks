import csv

raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
           1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]

row_list1 = [[0, 0, 'Header', 1, 1, 480], [1, 0, 'Start_track'], [1, 0, 'Time_signature', 4, 2, 24, 8], [1, 0, 'Key_signature', 0, 'major'], [1, 0, 'Tempo', 500000],
    [1, 0, 'Control_c', 9, 121, 0], [1, 0, 'Program_c', 9, 0], [1, 0, 'Control_c', 9, 7, 100], [1, 0, 'Control_c', 9, 10, 64], [1, 0, 'Control_c', 9, 91, 0], [1, 0, 'Control_c', 9, 93, 0], [1, 0, 'MIDI_port', 0]]
row_list2 = [[1, 159360, 'End_track'], [0, 0, 'End_of_file']]

with open('testtest3.csv', mode='w', newline='') as test_file:
    test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_writer.writerows(row_list1)

    for x in range(0, len(raw_seq)):
        if raw_seq[x] == 1:
            x *= 100
            test_writer.writerow(['1', x, 'Note_on_c', '9', '35', '35'])
            test_writer.writerow(['1', x+100, 'Note_off_c', '9', '35', '0'])

    test_writer.writerows(row_list2)


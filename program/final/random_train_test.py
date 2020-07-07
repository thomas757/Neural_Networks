# Written by Lotte Bouma (s3824853)

import random

# Randomly selects two songs to be used as testing data
list_of_songs = ["Hunting High Or Low", "Lonely Boy", "Obsession", "Cruel Summer", "Loverboy",
                 "Smokin In The Boys Room", "Turn Turn Turn", "Moonshadow"]
chosen_songs = random.sample(list_of_songs, 2)
print("The two songs to use for testing are: ", chosen_songs[0], " and ", chosen_songs[1])

import random

list_of_songs = ["Hunting High Or Low", "Ventura Highway", "Lonely Boy", "Obsession", "Cruel Summer", "Loverboy",
                 "Ride Captain Ride", "Smokin In The Boys Room", "Turn Turn Turn", "Moonshadow",
                 "I know Ill never love this", "Lets twist again"]
chosen_songs = random.sample(list_of_songs, 2)
print("The two songs to use for testing are: ", chosen_songs[0], " and ", chosen_songs[1])
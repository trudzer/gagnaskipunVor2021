import timamaelingar
import random

manager = timamaelingar.Stopwatch()
manager.starting_timer()

input_character ='c'

while input_character != 'n':
    random_int = random.randint(1,10000000)
    number = 0
    for i in range(10000000):
        number += 1
        if i == random_int:
            print("Random number:", random_int)
            print("random number time: " + str(manager.get_lap_time()))
            manager.pause_lap()
    manager.pause_time()
    print("I just ran the operation.")
    input_character = input("do you want to run the operation again (y/n)? ")
    manager.un_pause_time()
    manager.un_pause_lap()

manager.stop_time()

print("The time was: " + str(manager.get_duration()))
import time

class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.last_lap_time = 0
        self.paused_duration = 0
        self.paused_time = 0
        self.lap_paused_duration = 0
        
    def starting_timer(self):
        self.start_time = time.time()
        self.last_lap_time = self.start_time
        self.paused_time = 0
        self.lap_paused_duration = 0

    def stop_time(self):
        self.end_time = time.time()

    def get_lap_time(self):
        if self.last_lap_time == 0:
            self.last_lap_time = self.last_lap_time
        current_time = time.time()
        delta_time = current_time - self.last_lap_time - self.lap_paused_duration
        self.last_lap_time = current_time
        self.lap_paused_duration = 0
        return int((delta_time) * 10000)

    def get_time_from_start(self):
        return time.time() - self.start_time - self.paused_duration

    def pause_time(self):
        self.paused_time = time.time()

    def un_pause_time(self):
        self.paused_duration += time.time() - self.paused_time
        self.lap_paused_duration += time.time() - self.paused_time


    def get_duration(self):
        return self.end_time - self.start_time - self.paused_duration

if __name__ == "__main__":
    timer = Stopwatch()
    timer.starting_timer()
    number = 1
    print("Time of start: "  + str(timer.get_time_from_start()))
    for i in range(10000):
        number += 2
    for i in range(100000):
        if i % 10000 == 0 and i != 0:
            print("Lap of 10000: " + str(timer.get_lap_time()))
        number += 3
    timer.stop_time()
    print("Total program time: " + str(timer.get_duration()))
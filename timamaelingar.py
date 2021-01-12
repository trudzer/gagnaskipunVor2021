import time

class Stopwatch:
    def __init__(self):
        '''Initialize variables'''
        self.start_time = 0
        self.end_time = 0
        self.last_lap_time = 0
        self.paused_duration = 0
        self.paused_time = 0
        self.paused_lap_duration = 0
        self.paused_lap = 0
        
    def starting_timer(self):
        '''sets up variables'''
        self.start_time = time.time() #creates variable start_time that takes values from the library "time"
        self.last_lap_time = self.start_time #makes last_lap_time equivilent to the relevant start time
        self.paused_time = 0
        self.lap_paused_duration = 0

    def stop_time(self):
        '''creates end time'''
        self.end_time = time.time() #gets current time

    def get_lap_time(self):
        '''creates a lap which records time and resets'''
        if self.last_lap_time == 0: #if last_lap has no value
            self.last_lap_time = self.last_lap_time #last_lap becomes the last relevant time
        current_time = time.time() #makes current time equal to the current time
        delta_time = current_time - self.last_lap_time - self.paused_lap_duration #creates a variable which takes in the lap time, removing the extra time from other variables
        self.last_lap_time = current_time #makes last_lap equivilent to current time
        self.paused_lap_duration = 0 #resets paused time
        return delta_time

    def get_time_from_start(self):
        '''gets whole duration'''
        return time.time() - self.start_time - self.paused_time #returns current time minus extra time from pauses

    def pause_lap(self):
        '''pauses lap for program by creating a value which will be minused from total time'''
        self.paused_lap = time.time() #makes paused_lap equal to current time

    def un_pause_lap(self):
        '''unpauses lap and adds unpaused time to total time'''
        self.paused_lap_duration += time.time() - self.paused_lap #adds current time minus all the extra time when paused

    def pause_time(self):
        '''pauses time for program by creating a value which will be minused from total time'''
        self.paused_time = time.time()

    def un_pause_time(self):
        '''unpauses lap and adds unpaused time to total time'''
        self.paused_duration += time.time() - self.paused_time #adds current time minus all the extra time when paused


    def get_duration(self):
        '''gets total time for the whole program'''
        return self.end_time - self.start_time - self.paused_duration #returns current time minus the extra time when the program was stopped

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
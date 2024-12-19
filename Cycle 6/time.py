
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def display_time(self):
        print(f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}")

    def add_times(self, other):
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute + total_seconds // 60
        total_hours = self.__hour + other.__hour + total_minutes // 60
        total_seconds = total_seconds % 60
        total_minutes = total_minutes % 60
        total_hours = total_hours % 24
        return Time(total_hours, total_minutes, total_seconds)

def get_time_input():
    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))
    second = int(input("Enter second (0-59): "))
    return Time(hour, minute, second)

print("Enter the first time:")
time1 = get_time_input()

print("Enter the second time:")
time2 = get_time_input()

time3 = time1.add_times(time2)

print("The sum of the two times is:")
time3.display_time()


import datetime

class Time:
    def __init__(self):
        time_entry = input('Enter a time in hh:mm:ss format: ')
        self.__hours, self.__minutes, self.__seconds = map(int, time_entry.split(':'))
        print(datetime.time(self.__hours, self.__minutes, self.__seconds))

    def __add__(self, other):
   
        self_seconds = self.__hours * 60 * 60 + self.__minutes * 60 + self.__seconds
        other_seconds = other.__hours * 60 * 60 + other.__minutes * 60 + other.__seconds
        total_seconds = self_seconds + other_seconds
        return self.convert(total_seconds)

    def convert(self, seconds):
      
        seconds = seconds % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)


t1 = Time()
t2 = Time()


print(t1 + t2)

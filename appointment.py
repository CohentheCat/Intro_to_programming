# create a class named Appointment that contains instance variables startTime, endTime, dayOfWeek 
# (valid values are Sunday to Saturday, inclusive), and a date which consists of a day (valid values are 1 to 31, inclusive)
# a month (valid values are January to December, inclusive)
# and a year (valid values are 2021 through 2030). All times will be in military time (i.e. 24 hours clock time, where time starts at 0, 
# meaning 0000 and ends at 2359). Create the appropriate accessor and mutator methods, and any methods you may need.

import datetime
timeNow = datetime.datetime.now()
print(timeNow)

class Appointment:
    #Constructor method
    def __init__(self, startTime, endTime, dayOfWeek):
        self.startTime = startTime
        self.endTime = endTime
        self.dayOfWeek = dayOfWeek
    
    #Setter methods
    def setStartTime(self, startTime):
        self.startTime = startTime
    
    def setEndTime(self, endTime):
        self.endTime = endTime

    def setDayofWeek(self, dayOfWeek):
        self.dayOfWeek = dayOfWeek
    #getter methods
    def getStartTime(self, startTime):
        return self.startTime
    
    def getEndTime(self, endTime):
        return self.endTime

    def getDayofWeek(self, dayOfWeek):
        return self.dayOfWeek

    



    def make_appointment():
        hour_max = 23
        min_max = 59
        dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = { "January" : 31, 
                   "February" : 28, 
                   "March" : 31,
                   "April" : 30, 
                   "May" : 31,
                   "June" : 30,
                   "July" : 31, 
                   "August" : 31, 
                   "September" : 30, 
                   "October" : 31, 
                   "November" : 30, 
                   "December" : 31 }

        
        user_dow = input("What day is this appoinment for?: ").capitalize()
        while user_dow not in dow:
            user_dow = input("Please enter a valid day of the week").capitalize()

        user_month = input("what month?: ").capitalize()
        while user_month not in months:
            user_month = input("Please enter a valid month: ").capitalize()
        if user_month in months:
            date_limit = months[user_month]
        
        user_date = int(input("What date?: "))
        while user_date > date_limit:
            user_date = int(input("Sorry there are only {} days in {}: ".format(date_limit, user_month)))
        
        user_time = int(input("What time?(HHMM): "))
        while user_time < 0000 or user_time > 2359:
            user_time = int(input("Please enter a valid time(HHMM): "))
        

        
        

e = Appointment.make_appointment()

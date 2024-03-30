# Author: David Miller | djm545
# Date: 5/31/23
# Purpose: Birthday Class

class Birthday:
    def __init__(self, month, day, year):
        self.__month = month
        self.__day = day
        self.__year = year
    
    def getDay(self):
        return self.__day
    def getMonth(self):
        return self.__month
    def getYear(self):
        return self.__year
    
    def __str__(self):
        return f"{self.__month}/{self.__day}/{self.__year}"
    
    def __hash__(self):
        return (self.__day + self.__month + self.__year) % 12
    
    def __eq__(self, other):
        return True if self.__day == other.getDay() and self.__month == other.getMonth() and self.__year == other.getYear() else False
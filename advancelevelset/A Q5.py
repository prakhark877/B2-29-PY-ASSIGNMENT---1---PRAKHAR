class Time:
    def __init__(self,hours,minute):
        self.hours = hours 
        self.minute = minute
        self.tmin = hours*60 + minute

    def addTime(self, time2 ):
        self.totalmin = self.minute  + time2.minute 
        if (self.totalmin >= 60):

            self.totalhrs = self.hours  + time2.hours + self.totalmin//60
            self.totalmin = (self.minute + time2.minute)%60
        else:
            self.totalhrs = self.hours + time2.hours 
            self.totalmin = self.minute +time2.minute
            
        self.tmin += time2.tmin 
    def displayTime(self):
        print( f"{self.totalhrs} hrs {self.totalmin} min" )

    def displayMinute(self):
        print(f"Total minutes: { self.tmin}") 
    
t1= Time(12,50)
t2 = Time(2,20)
t1.addTime(t2)
t1.displayTime()
t1.displayMinute()

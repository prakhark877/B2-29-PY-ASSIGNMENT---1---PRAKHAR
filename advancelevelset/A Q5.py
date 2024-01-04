class Timing:
    def __init__(self,hours,minute):
        self.hours = hours
        self.minute = minute
        self.tmin = hours*60 + minute

    def addTiming(self, time2 ):
        self.totamin = self.minute  + time2.minute
        if (self.totamin >= 60):

            self.totahrs = self.hours  + time2.hours + self.totamin//60
            self.totamin = (self.minute + time2.minute)%60
        else:
            self.totahrs = self.hours + time2.hours
            self.totamin = self.minute +time2.minute

        self.tmin += time2.tmin
    def displayTiming(self):
        print( f"{self.totahrs} hrs {self.totamin} min" )

    def displayMinute(self):
        print(f"Total minutes: { self.tmin}")

ta= Timing(12,50)
tb = Timing(2,20)
ta.addTiming(tb)
ta.displayTiming()
ta.displayMinute()

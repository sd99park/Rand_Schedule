class Employees:

    def __init__(self, Name):
        self.DaysOff = []
        self.DaysWorking = []
        self.Name = Name
        self.TotalDaysWorking = 0

    def DaysWorkingLength(self):
        return len(self.DaysWorking)

    def AddDayOff(self, Day):
        if Day == "M":
            self.DaysOff.append(0)
            self.TotalDaysWorking += 1
        elif Day == "T":
            self.DaysOff.append(1)
            self.TotalDaysWorking += 1
        elif Day == "W":
            self.DaysOff.append(2)
            self.TotalDaysWorking += 1
        elif Day == "R":
            self.DaysOff.append(3)
            self.TotalDaysWorking += 1
        elif Day == "F":
            self.DaysOff.append(4)
            self.TotalDaysWorking += 1
        elif Day == "S":
            self.DaysOff.append(5)
            self.TotalDaysWorking += 1
        elif Day == "U":
            self.DaysOff.append(6)
            self.TotalDaysWorking += 1

    def AddDayWorking(self, Day):
        self.DaysWorking.append(Day)
        self.TotalDaysWorking += 1

    def DeleteShift(self, Day):
        self.DaysWorking.remove(Day)
        self.TotalDaysWorking -= 1

    # GetDaysOff?

    # GetDaysWorking?

    def AbleToWork(self, Day):
        NotWorking = True
        for i in range(len(self.DaysOff)):
            if Day == self.DaysOff[i]:
                NotWorking = False

        for i in range(len(self.DaysWorking)):
            if Day == self.DaysWorking[i]:
                NotWorking = False

        return NotWorking

    # GetTotalDaysWorking?


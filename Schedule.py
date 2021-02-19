from Employees import *
import random


class Schedule:

    def __init__(self):
        self.EmployeeList = []
        self.DailyWorkers = [[], [], [], [], [], [], []]

    def Readfile(self, filename): # Reads the txt file of form 'Name, Day, Day, Dya'
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            i = 0
            name = ""
            while line[i] != ',':
                name = name + line[i]
                i += 1
            print(name)
            person = Employees(name)
            line = line.replace(name, "")
            line = line.replace(" ", "")
            line = line.replace(",", "")
            for letter in line:
                person.AddDayOff(letter)
            self.EmployeeList.append(person)

    def RandomSchedule(self, OpenShifts):  # Creates a random un-even schedule
        for i in range(7):  # for all days of the week
            j = 0
            while j < OpenShifts:  # While there are still open shifts left
                RandomEmployee = random.randint(0, len(self.EmployeeList) - 1)
                if self.EmployeeList[RandomEmployee].AbleToWork(i):  # If the are able to work, schedule them
                    self.DailyWorkers[i].append(self.EmployeeList[RandomEmployee])
                    self.EmployeeList[RandomEmployee].AddDayWorking(i)
                    j += 1

    def ShowEmployeeList(self):
        for i in self.EmployeeList:
            print(i.Name)

    def ShowDailyWorkers(self):
        for i in range(7):
            print("Day " + str(i+1))
            for Emp in self.DailyWorkers[i]:
                print(Emp.Name)

    # given two workers, give the person with the least shifts one of other persons shifts
    def SwitchShift(self, LessShifts, MoreShifts):
        RandInt = random.randint(0, len(MoreShifts.DaysWorking) - 1)
        RandDay = MoreShifts.DaysWorking[RandInt]
        while not LessShifts.AbleToWork(RandDay): # find a random day that moreshifts works but less shifts isnt
            RandInt = random.randint(0, len(MoreShifts.DaysWorking) - 1)
            RandDay = MoreShifts.DaysWorking[RandInt]

        # switch the shifts
        self.SwitchDailyWorkers(MoreShifts, LessShifts, RandDay)
        LessShifts.AddDayWorking(RandDay)
        MoreShifts.DeleteShift(RandDay)

    # Swap the two people working at that specific day
    def SwitchDailyWorkers(self, OldWorker, NewWorker, Day):
        self.DailyWorkers[Day].remove(OldWorker)
        self.DailyWorkers[Day].append(NewWorker)

    def WorkingMost(self):
        Most = self.EmployeeList[0]
        for i in range(len(self.EmployeeList)):
            if self.EmployeeList[i].TotalDaysWorking > Most.TotalDaysWorking:
                Most = self.EmployeeList[i]

        return Most

    def WorkingLeast(self):
        Least = self.EmployeeList[0]
        for i in range(len(self.EmployeeList)):
            if self.EmployeeList[i].TotalDaysWorking < Least.TotalDaysWorking:
                Least = self.EmployeeList[i]

        return Least

    # even out the un-even schedule created by RandomSchedule
    def EvenSchedule(self):
        while self.WorkingMost().TotalDaysWorking - self.WorkingLeast().TotalDaysWorking > 2:
            self.SwitchShift(self.WorkingLeast(), self.WorkingMost())

    def ShowTotalDaysWorking(self):
        for i in range(len(self.EmployeeList)):
            print(self.EmployeeList[i].Name + ": " + str(self.EmployeeList[i].TotalDaysWorking) + "\n")

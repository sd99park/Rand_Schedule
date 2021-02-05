from Employees import *
import random


class Schedule:

    def __init__(self):
        self.EmployeeList = []
        self.DailyWorkers = [[], [], [], [], [], [], []]

    def Readfile(self, filename):
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


    def RandomSchedule(self, OpenShifts):
        for i in range(7):
            j = 0
            while j < OpenShifts:
                RandomEmployee = random.randint(0, len(self.EmployeeList) - 1)
                if self.EmployeeList[RandomEmployee].AbleToWork(i):
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

    def SwitchShift(self, LessShifts, MoreShifts):
        RandInt = random.randint(0, len(MoreShifts.DaysWorking) - 1)
        RandDay = MoreShifts.DaysWorking[RandInt]
        while not LessShifts.AbleToWork(RandDay):
            RandInt = random.randint(0, len(MoreShifts.DaysWorking) - 1)
            RandDay = MoreShifts.DaysWorking[RandInt]

        self.SwitchDailyWorkers(MoreShifts, LessShifts, RandDay)
        LessShifts.AddDayWorking(RandDay)
        MoreShifts.DeleteShift(RandDay)

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


    def EvenSchedule(self):
        while self.WorkingMost().TotalDaysWorking - self.WorkingLeast().TotalDaysWorking > 2:
            self.SwitchShift(self.WorkingLeast(), self.WorkingMost())

    def ShowTotalDaysWorking(self):
        for i in range(len(self.EmployeeList)):
            print(self.EmployeeList[i].Name + ": " + str(self.EmployeeList[i].TotalDaysWorking) + "\n")



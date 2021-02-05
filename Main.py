from Schedule import *

OpenShifts = 8
print("Test")
S = Schedule()

print("Read fake file")
S.Readfile("data.txt")

S.ShowEmployeeList()

S.RandomSchedule(6)
S.ShowTotalDaysWorking()
S.ShowDailyWorkers()

S.EvenSchedule()
print("\n")
S.ShowTotalDaysWorking()
S.ShowDailyWorkers()
print("\n")
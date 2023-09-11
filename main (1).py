# 1.2 leap year


year%4==0&
year%100!=0/
year%400==0


def isleap year(year):
if(year%4==0andyear%100!=0)or (year%400==0):
  return true
 return false
else:

year=int(input("Enter a year:"))

if isleap year(year):
print("{}is a leap year".format(year))
else:
print("{}is not a leap year".format(year))

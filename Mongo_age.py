def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    yearsToDays = ((currentYear-1)-birthYear)*390
    if currentMonth > birthMonth:
        daysUntilNextBirthday = 26*(((15-currentMonth)+birthMonth)-1)+(26-currentDay)+(birthDay)
    else:
        daysUntilNextBirthday = 26*(((15-currentMonth)+birthMonth)-16)+(26-currentDay)+(birthDay)
    age = (((390 - daysUntilNextBirthday)+yearsToDays)/390)
    return age

a = float(input("Please enter your birth year: "))
b = float(input("Please enter your birth month: "))
c = float(input("Please enter your birth day: "))
d = float(input("Please enter the current year: "))
e = float(input("Please enter the current month: "))
f = float(input("Please enter the current day: "))

ans = compute_mongo_age(a, b, c, d, e, f)
print("You are " + str(ans) + " Mongo years old.")

import json
import datetime

def load_days():
    with open('data.json') as days_of_week:
        days = json.load(days_of_week)
    return days

print(type(load_days()))
days = load_days()
print(days)

days["week"]["Avarage"]["start_time"] = float(input("What is the avarage time in week, that you are busy? please insert only numbers (sample 8:30 pm is 8.30)"))
diff = days["week"]["Avarage"]["end_time"] - days["week"]["Avarage"]["start_time"]
number_of_deadlines = int(input("How many deadlines do you have this week?"))
x = datetime.datetime.now()
for i in range (0,number_of_deadlines):
    day = input("On which day of the week is it? (Please insert in the following way: Monday,Tuesday etc.)")
    print(day)
    days["week"][day]["Deadline"]["title"] = input("What subject is it from?")
    days["week"][day]["Deadline"]["time"] = float(input("At what time is the deadline?"))
    days["week"][day]["Deadline"]["duration"] =  float(input("How long you think it will take in hours"))

def save_to_the_file(days):
    f = open("data.json","w")
    f.write(json.dumps(days,indent = 2))
    f.close()
save_to_the_file(days)

def check_deadline(day):
    if(days["week"][day]["Deadline"]["time"]):
        return 1
    else:
        return 0

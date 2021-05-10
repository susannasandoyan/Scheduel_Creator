import json
import datetime

def load_days():
    with open('data.json') as days_of_week:
        days = json.load(days_of_week)
    return days

weekdays = []
days = load_days()

def check_deadline(day):
    if(days["week"][day]["Deadline"]["time"]):
        return 1
    else:
        return 0

def day_of_week(num):
    arr = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return arr[num]

def save_to_the_file(days):
    f = open("data.json","w")
    f.write(json.dumps(days,indent = 2))
    f.close()

def textToNum(text):
    arr = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for i in range (0 ,len(arr)):
        if(text == arr[i]):
            return i
def main():

    print("Hello! Please answer to all questions carefully and follow the formats that are given \n ")
    print ("Please be informed , if you want a deadline to be scheduled you have to insert at least one day before it\n")
    print("Program works only for one week, and you can register only one deadline on each day \n")
    days["week"]["Avarage"]["start_time"] = float(input("What is the avarage time in week, that you are busy? please insert only numbers (sample 8:30 pm is 8.30)"))
    diff = days["week"]["Avarage"]["end_time"] - days["week"]["Avarage"]["start_time"]
    number_of_deadlines = int(input("How many deadlines do you have this week? \n"))
    #-------------------------------------------------------------------------------------
    #day_text = day_of_week(datetime.datetime.today().weekday())
    #day_num = datetime.datetime.today().weekday()
    day_num = 0
    for i in range (0,number_of_deadlines):
        strr = str(i + 1)
        print("Please answer to the following few question for the deadline that you have \n")
        day = input("On which day of the week is your deadline "+ strr +" ? (Please insert in the following way: Tuesday,Thursday etc.) \n")
        if (day == "Monday"):
            print("You cannot insert Monday")
            continue
        if(textToNum(day) < day_num):
            print("Your Deadline was passed")
            continue
        elif(textToNum(day) > day_num):
            weekdays.append(day)
            days["week"][day]["Deadline"]["title"] = input("What subject is it from? \n")
            days["week"][day]["Deadline"]["time"] = float(input("At what time is the deadline?(please insert only numbers, e.g. 5pm = 5) \n"))
            days["week"][day]["Deadline"]["duration"] =  float(input("How long you think it will take in hours (please insert only numbers, e.g. 2 hours = 2) \n"))

    save_to_the_file(days)

    for i in range (0,number_of_deadlines):
        time_need = days["week"][weekdays[i]]["Deadline"]["duration"]
        if(time_need < diff):
            day_in_text = day_of_week(textToNum(weekdays[i]) - 1)
            days["week"][weekdays[i]]["Deadline"]["schedule_start"]["Day"] = day_in_text
            days["week"][weekdays[i]]["Deadline"]["schedule_start"]["sttime"] = days["week"]["Avarage"]["start_time"]

    for i in range (0,number_of_deadlines):
        print("You can start your assignment of " + str(days["week"][weekdays[i]]["Deadline"]["title"]) + " on " + str(days["week"][weekdays[i]]["Deadline"]["schedule_start"]["Day"]) + " at " + str(days["week"]["Avarage"]["start_time"]) + " pm \n"
      )


if __name__ == '__main__':
    main()
import json
import datetime

def load_days():
    with open('data.json') as days_of_week:
        days = json.load(days_of_week)
    return days

weekdays = []
days = load_days()

def str_to_time(string):
    i = 1
    j = 1
    flot = string[0]
    while(i < len(string)):
        if(string[i] == ":"):
            while(j<i):
                flot = flot + string[j]
                j +=1
            break
        i+=1
    i+=1
    flot = flot + "."
    while(i<len(string)):
        flot +=string[i]
        i+=1
    return float(flot)
    
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
    days["week"]["Avarage"]["start_str"] = input("Untill what time in the week in avarage,are you busy? Insert in the following way : 12:00 pm = 12:00,3:30 pm = 3:30 etc.)\n")
    days["week"]["Avarage"]["start_time"] = str_to_time(days["week"]["Avarage"]["start_str"])
    diff = days["week"]["Avarage"]["end_time"] - days["week"]["Avarage"]["start_time"]
    number_of_deadlines = int(input("How many deadlines do you have this week?\n"))
    #-------------------------------------------------------------------------------------
    day_text = day_of_week(datetime.datetime.today().weekday())
    day_num = datetime.datetime.today().weekday()
    for i in range (0,number_of_deadlines):
        strr = str(i + 1)
        print("Please answer to the following few question for the deadline that you have \n")
        day = input("On which day of the week is your deadline "+ strr +" ? (Please insert in the following way: Tuesday,Thursday etc.) \n")
        if (day == "Monday"):
            print("You cannot insert Monday")
            quit()
        if(textToNum(day) < day_num):
            print("Your Deadline was passed")
            continue
        elif(textToNum(day) > day_num):
            weekdays.append(day)
            days["week"][day]["Deadline"]["title"] = input("What subject is it from? \n")
            days["week"][day]["Deadline"]["time"] = str_to_time(input("At what time is the deadline?(Insert in the following way : 12:20,3:30, 12:00 etc.) \n")) 
            days["week"][day]["Deadline"]["duration"] =  float(input("How long you think it will take in hours (please insert only numbers, e.g. 2 hours = 2) \n"))

    save_to_the_file(days)

    for i in range (0,number_of_deadlines):
        time_need = days["week"][weekdays[i]]["Deadline"]["duration"]
        if(time_need < diff):
            day_in_text = day_of_week(textToNum(weekdays[i]) - 1)
            days["week"][weekdays[i]]["Deadline"]["schedule_start"]["Day"] = day_in_text
            days["week"][weekdays[i]]["Deadline"]["schedule_start"]["sttime"] = days["week"]["Avarage"]["start_str"]

    for i in range (0,number_of_deadlines):
        print("You can start your assignment of " + str(days["week"][weekdays[i]]["Deadline"]["title"]) + " on " + str(days["week"][weekdays[i]]["Deadline"]["schedule_start"]["Day"]) + " at " + str(days["week"]["Avarage"]["start_str"]) + " pm \n"
      )


if __name__ == '__main__':
    main()
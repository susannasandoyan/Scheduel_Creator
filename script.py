import json

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

def add_deadline():
    for i in range(0,number_of_deadlines-1):
        deadline = {
            "Subject" : input("What subject is it from?"),
            "Duration" : float(input("How long you think it will take in hours")),
            "Day" : input("On which day of the week is it? (Please insert in the following way: Monday,Tuesday etc.)"),
            "End_time" : float(input("At what time is the deadline?"))
        }




# arr = [[0]*4]*number_of_deadlines
# for i in range (0,number_of_deadlines-1):
#     arr[i][0] = input("What subject is it from?")
#     arr[i][1] = float(input("How long you think it will take in hours"))
#     arr[i][2] = input("On which day of the week is it? (Please insert in the following way: Monday,Tuesday etc.)")
#     arr[i][3] = float(input("At what time is the deadline?"))

# print(arr)

#!/usr/bin/python
import datetime

p = [
    (datetime.time(9, 0), datetime.time(9, 50)),        #0
    (datetime.time(9, 50), datetime.time(10, 40)),      #1
    (datetime.time(10, 40), datetime.time(11, 30)),     #2
    (datetime.time(11, 30), datetime.time(12, 20)),     #3
    (datetime.time(12, 20), datetime.time(13, 10)),     #4
    (datetime.time(14, 0), datetime.time(14, 50)),      #5
    (datetime.time(14, 50), datetime.time(15, 40)),     #6
    (datetime.time(15, 40), datetime.time(16, 30)),     #7
]

schedule = [
    [
        [p[0], "Electrical", "lecture"],
        [p[1], "Energy", "lecture"],
        [p[2], "Mechanics", "lecture"],
        [p[3], "Energy", "lecture"]
    ],
    [
        [p[0], "Maths", "lecture"],
        [p[1], "Electrical", "tutorial"],
        [p[2], "Energy", "lecture"],
        [p[3], "Mechanics", "lecture"],
        [p[4], "Mechanics", "tutorial"],
        [p[6], "Chemistry", "lecture"],
    ],
    [
        [p[0], "Electrical", "lecture"],
        [p[1], "Electrical", "lab"],
        [p[2], "Electrical", "lab"],
        [p[5], "Maths", "lecture"],
        [p[6], "OOP", "lecture"],
        [p[7], "Chemistry", "tutorial"],
    ],
    [
        [p[0], "Electrical", "lecture"],
        [p[1], "OOP", "lecture"],
        [p[2], "Chemistry", "lecture"],
        [p[4], "Maths", "tutorial"],
        [p[5], "Chemistry", "lecture"],
    ],
    [
        [p[0], "Maths", "lecture"],
        [p[1], "OOP", "lecture"],
        [p[2], "Electrical", "lecture"],
        [p[3], "OOP", "lab"],
        [p[4], "OOP", "lab"],
        [p[5], "Chemistry", "lab"],
    ]
]

weekday = datetime.date.today().weekday()
time = datetime.datetime.now().time()
duration = datetime.timedelta(minutes=50)

def add_time(time, timedelta):
    return (datetime.datetime.combine(datetime.datetime(1,1,1), time) + timedelta).time()

def lies_within(t, time):
    if (t[0] <= time < t[1]) : return True

def get_current_period():
    todays_schedule = schedule[weekday]

    for period in todays_schedule:
        if lies_within(period[0], time):
            return period

def get_upcoming_period():
    todays_schedule = schedule[weekday]
    
    for period in todays_schedule:
        if time < period[0][0]:
            return period

if (weekday not in [5, 6]):
    current_period = get_current_period()
    upcoming_period = get_upcoming_period()
    if current_period or upcoming_period:
        if current_period:
            print(f"Ongoing {current_period[1]} {current_period[2]}", end="  ")
        if upcoming_period:
            print(f"Upcoming {upcoming_period[1]} {upcoming_period[2]} at {upcoming_period[0][0].strftime('%H:%M')}")

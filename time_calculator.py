def add_time(start, duration, starting_weekday = None):

    #extraction of relevant parameters--start time
    start_colon = start.find(":")
    start_space = start.find(" ")
    start_hour = int(start[: start_colon])
    start_min = int(start[start_colon + 1: start_space])
    start_am_pm = start[start_space + 1 : ]

    #extraction of relevant parameters--duration time
    duration = duration.split(":")
    dur_hour = int(duration[0])
    dur_min = int(duration[1])

    #incorporating additional days

    days_to_add = dur_hour // 24 #this stores the whole days as a separate variable--only stores the quotient!
    dur_hour = dur_hour % 24 #this gives the leftover hours, once the whole days are taken out

    #addition of duration time to start time
    end_min = start_min + dur_min
    end_hour = 0
    if end_min >= 60:
        end_min = end_min - 60
        end_hour += 1

    end_hour = end_hour + start_hour + dur_hour

    #switch between am/pm
    end_am_pm = start_am_pm

    if end_hour >= 12:
        if start_am_pm == "AM":
            end_am_pm = "PM"
        else:
            end_am_pm = "AM" #switch between PM and AM = crossing midnight--add a day here
            days_to_add += 1

    if end_hour >= 13:
        end_hour = end_hour - 12

    #getting the printout of the additional days in correct format
    extra_days = ""
    if days_to_add < 1:
        extra_days ==""
    elif days_to_add == 1:
        extra_days = "(next day)"
    else:
        extra_days = "(%d days later)" %(days_to_add)

    #getting final output, without days of week
    #in some instances the minutes aren't 2-figure integers--in these cases, zfill puts a padding 0 on the front
    new_time = str(end_hour) + ":" + str(end_min).zfill(2) + " " + end_am_pm+ " " + extra_days
    new_time = new_time.rstrip()

    #day of the week
    end_weekday = ""
    if starting_weekday != None:
        # calculate how many days remain, after whole weeks are taken out
        remaining_days = days_to_add % 7

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        #making the input case-insensitive
        starting_weekday = starting_weekday.lower()
        starting_weekday = starting_weekday.capitalize()

        start_index = weekdays.index(starting_weekday)

        for count, day in enumerate(weekdays[start_index:]):

            if count == remaining_days:
                end_weekday = day

        new_time = str(end_hour) + ":" + str(end_min).zfill(2) + " " + end_am_pm + ", " + end_weekday + " " + extra_days
        new_time = new_time.rstrip()

    return new_time

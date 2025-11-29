"""

Sleep Tracker Program

Analyzes weekly sleep patterns then provides personalized recommendations

"""

import time #for some time delays to make the program clean



def sleeptracker():

    

    #Collect the sleep data for each day of the week

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]



    #tracking variables

    total_sleep = 0

    sleep_times = []

    total_caffeine = 0

    total_screentime = 0

    total_stress = 0



    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    print("|    Welcome to your personal Sleep Tracker Program!    |")

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    time.sleep(1)

    print("""\n    The goal of this sleep tracker is to take in various factors that contribute to 

    overall sleep quality and tell you what yours is like, while also letting you know 

    what areas appear to be lacking.""")

    time.sleep(2.5)



    #This will loop through all the days of the week

    for day in days:

        print(f"\n--- [{day}] ---")



        #Getting hours of sleep

        while True:

            try:

                hours = float(input(f"\nHow many hours of sleep did you get on {day}?\nHours: "))

                if hours >= 0 and hours <= 24:

                    total_sleep += hours

                    break

                else:

                    print("Please enter a value between 0 and 24 hours.\n")

            except ValueError:

                print("\nPlease enter a valid number.\n")



        #Getting what time they went to sleep (military time)

        while True:

            try:

                sleep_time = float(input("\nWhat time did you go to sleep? (military time, e.g., 10:30PM = 22.5)\nSleep Time: "))

                if sleep_time >= 0 and sleep_time <=24:

                    sleep_times.append(sleep_time)

                    break

                else:

                    print("Please enter a value between 0 and 24 hours.\n")

            except ValueError:

                print("\nPlease enter a valid number.\n")



        #Getting caffeine consumption

        while True:

            try:

                caffeine = int(input("\nDid you drink caffeine within 8 hours of going to sleep? (1=Yes, 0=No)\nAnswer: "))

                if caffeine == 1 or caffeine == 0:

                    total_caffeine += caffeine

                    break

                else:

                    print("Please enter a value of 1 or 0.\n")

            except ValueError:

                print("\nPlease enter a valid number.\n")



        #Getting screen time

        while True:

            try:

                screen = int(input("\nDid you look at your phone or any screen 30 minutes before going to sleep? (1=Yes, 0=No)\nAnswer: "))

                if screen == 1 or screen == 0:

                    total_screentime += screen

                    break

                else:

                    print("Please enter a value of 1 or 0.\n")

            except ValueError:

                print("\nPlease enter a valid number.\n")



        #Getting stress level

        while True:

            try:

                stress = int(input("\nHow stressed did you feel? (scale 1-10)\nAnswer: "))

                if stress >= 1 and stress <= 10:

                    total_stress += stress

                    break

                else:

                    print("Please enter a value of 1 to 10.\n")

            except ValueError:

                print("\nPlease enter a valid number.\n")

    

    return total_sleep, sleep_times, total_caffeine, total_screentime, total_stress





def calculate_sleep_difference(sleep_times):

    #calculating the sleep difference in sleep times across the week

    total_diff = 0

    for i in range(1, len(sleep_times)):

        diff = sleep_times[i] - sleep_times[i-1]

        if diff > 12:

            diff = diff - 24

        elif diff < -12:

            diff = diff + 24

        total_diff += abs(diff)



    return total_diff / (len(sleep_times) - 1)



def anlayze_sleep_quality(avg_sleep_diff, avg_sleep_hours, avg_caffeine, avg_screentime, avg_stress_level):

    #All of the if statements that give reccomendations based on the results

    time.sleep(1)

    print("\n=================================================")

    print("SLEEP ANALYSIS RESULTS")

    print("=================================================")

    time.sleep(1)

    print(f"\nYour weekly averages: ")

    print(f"  - Average sleep hours: {avg_sleep_hours:.1f} hours")

    time.sleep(.5)

    print(f"  - Sleep time consistency: {avg_sleep_diff:.1f} hours variation")

    time.sleep(.5)

    print(f"  - Caffeine before bed: {avg_caffeine:.1f} times per week")

    time.sleep(.5)

    print(f"  - Screen time before bed: {avg_screentime:.1f} times per week")

    time.sleep(.5)

    print(f"  - Average stress level: {avg_stress_level:.1f}/10")

    time.sleep(1.5)



    print("\n=================================================")

    print("Recommendations")

    print("=================================================")

    print("\nFrom the data you entered we can make some conclusions about your sleep quality, ")

    print("we have some recommendations if some areas could use improvement!")

    time.sleep(1.5)

    #recommendations thread

    recommendations = []



    if avg_sleep_diff > 2:

        recommendations.append("sleep at more consistent times")

    if avg_sleep_hours < 7:

        recommendations.append("get at least 7 hours of a sleep a day")

    if avg_caffeine > 2:

        recommendations.append("drink less caffeine before you go to sleep")

    if avg_screentime > 3:

        recommendations.append("look at your phone less before you go to bed")

    if avg_stress_level > 4:

        recommendations.append("try and manage stress better")



    #Displaying the recommendations

    if recommendations: #Meaning if there is at least one recommendation in the list

        if len(recommendations) == 1:

            print("It's recommended that you " + recommendations[0] + ".")

        else:

            print("It's recommended that you " + "," .join(recommendations[:-1]) + ", and " + recommendations[-1] + ".")

    else:

        print("Your sleep quality looks healthy overall!")



    #Some additional context

    time.sleep(2.5)

    print("\n==============================")

    print("ADDITIONAL CONTEXT")

    print("==============================")

    if avg_sleep_hours >= 7 and avg_sleep_hours <= 9:

        print("Your sleep duration is within the recommended range (7-9 hours)")

    elif avg_sleep_hours < 7:

        print("You're getting less than the recommended 7-9 hours of sleep")

    else:

        print("You may be oversleeping (more than 9 hours on average)")

    

    if avg_sleep_diff <= 2:

        print("Your sleep schedule is relatively consistent")

    else:

        print("Your sleep times vary significantly day-to-day")

    

    if avg_caffeine <= 2:

        print("Your caffeine intake before bed is minimal")

    else:

        print("Frequent caffeine consumption before bed may affect sleep quality")

    

    if avg_screentime <= 3:

        print("You're limiting screen exposure before bed")

    else:

        print("Frequent screen time before bed can disrupt your sleep")

    

    if avg_stress_level <= 4:

        print("Your stress levels are relatively low")

    elif avg_stress_level <= 7:

        print("Moderate stress levels may be affecting your sleep")

    else:

        print("High stress levels are likely impacting your sleep quality")



def main(): #main function

    total_sleep, sleep_times, total_caffeine, total_screentime, total_stress = sleeptracker()



    #averages

    days_in_week = 7

    avg_sleep_hours = total_sleep / days_in_week

    avg_sleep_diff = calculate_sleep_difference(sleep_times)

    avg_caffeine = total_caffeine 

    avg_screen_time = total_screentime

    avg_stress_level = total_stress / days_in_week



    anlayze_sleep_quality(avg_sleep_diff, avg_sleep_hours, avg_caffeine, avg_screen_time, avg_stress_level)



    print("\n\nThank you")



main()

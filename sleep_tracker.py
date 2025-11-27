#!/usr/bin/env python3
"""
Sleep Tracker Program
Analyzes weekly sleep patterns and provides personalized recommendations
"""

def get_sleep_data():
    """Collect sleep data for each day of the week"""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Initialize tracking variables
    total_sleep = 0
    sleep_times = []
    total_caffeine = 0
    total_screen_time = 0
    total_stress = 0
    
    print("Welcome to Your Beloved Sleep Tracker!")
    print("\nThe goal of this sleep tracker is to take in various factors that contribute to")
    print("overall sleep quality and tell you how your overall sleep quality is, and any")
    print("recommendations if your sleep quality seems to be lacking.")
    print("\nPlease start with answering the following questions:")
    print("=" * 60)
    
    for day in days:
        print(f"\n--- {day} ---")
        
        # Get hours of sleep
        while True:
            try:
                hours = float(input(f"How many hours of sleep did you get on {day}? "))
                if hours >= 0 and hours <= 24:
                    total_sleep += hours
                    break
                else:
                    print("Please enter a value between 0 and 24 hours.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get sleep time (military time)
        while True:
            try:
                sleep_time = float(input(f"What time did you go to sleep? (military time, e.g., 22.5 for 10:30 PM): "))
                if 0 <= sleep_time <= 24:
                    sleep_times.append(sleep_time)
                    break
                else:
                    print("Please enter a time between 0 and 24.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get caffeine consumption
        while True:
            try:
                caffeine = int(input(f"Did you drink caffeine within 8 hours before sleep? (1=Yes, 0=No): "))
                if caffeine in [0, 1]:
                    total_caffeine += caffeine
                    break
                else:
                    print("Please enter 1 for Yes or 0 for No.")
            except ValueError:
                print("Please enter 1 or 0.")
        
        # Get screen time
        while True:
            try:
                screen = int(input(f"Did you look at your phone 30 minutes before sleep? (1=Yes, 0=No): "))
                if screen in [0, 1]:
                    total_screen_time += screen
                    break
                else:
                    print("Please enter 1 for Yes or 0 for No.")
            except ValueError:
                print("Please enter 1 or 0.")
        
        # Get stress level
        while True:
            try:
                stress = int(input(f"How stressed did you feel on {day}? (scale 1-10): "))
                if 1 <= stress <= 10:
                    total_stress += stress
                    break
                else:
                    print("Please enter a value between 1 and 10.")
            except ValueError:
                print("Please enter a valid integer between 1 and 10.")
    
    return total_sleep, sleep_times, total_caffeine, total_screen_time, total_stress


def calculate_sleep_difference(sleep_times):
    """Calculate average difference in sleep times across the week"""
    if len(sleep_times) < 2:
        return 0
    
    total_diff = 0
    for i in range(1, len(sleep_times)):
        diff = sleep_times[i] - sleep_times[i-1]
        # Handle midnight crossing (modulo 24)
        if diff > 12:
            diff = diff - 24
        elif diff < -12:
            diff = diff + 24
        total_diff += abs(diff)
    
    return total_diff / (len(sleep_times) - 1)


def analyze_sleep_quality(avg_sleep_diff, avg_sleep_hours, avg_caffeine, avg_screen_time, avg_stress_level):
    """Analyze sleep quality and provide recommendations"""
    
    print("\n" + "=" * 60)
    print("SLEEP ANALYSIS RESULTS")
    print("=" * 60)
    print(f"\nYour weekly averages:")
    print(f"  • Average sleep hours: {avg_sleep_hours:.1f} hours")
    print(f"  • Sleep time consistency: {avg_sleep_diff:.1f} hours variation")
    print(f"  • Caffeine before bed: {avg_caffeine:.0f} times per week")
    print(f"  • Screen time before bed: {avg_screen_time:.0f} times per week")
    print(f"  • Average stress level: {avg_stress_level:.1f}/10")
    
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)
    print("\nFrom the data you entered we can make some conclusions about your")
    print("quality of sleep, along with some recommendations if some areas")
    print("could use some improvement!\n")
    
    # Build recommendations based on thresholds
    recommendations = []
    
    if avg_sleep_diff > 2:
        recommendations.append("sleep at more consistent times")
    if avg_sleep_hours < 7:
        recommendations.append("get at least 7 hours of sleep a day")
    if avg_caffeine > 2:
        recommendations.append("drink less caffeine before you go to sleep")
    if avg_screen_time > 3:
        recommendations.append("look at your phone before you go to bed less")
    if avg_stress_level > 4:
        recommendations.append("try and manage stress better")
    
    # Display recommendations
    if recommendations:
        print("It's recommended that you " + ", ".join(recommendations) + ".")
    else:
        print("Your sleep habits look healthy overall!")
    
    # Provide additional context
    print("\n" + "-" * 60)
    print("ADDITIONAL INSIGHTS:")
    
    if avg_sleep_hours >= 7 and avg_sleep_hours <= 9:
        print("✓ Your sleep duration is within the recommended range (7-9 hours)")
    elif avg_sleep_hours < 7:
        print("⚠ You're getting less than the recommended 7-9 hours of sleep")
    else:
        print("⚠ You may be oversleeping (more than 9 hours on average)")
    
    if avg_sleep_diff <= 2:
        print("✓ Your sleep schedule is relatively consistent")
    else:
        print("⚠ Your sleep times vary significantly day-to-day")
    
    if avg_caffeine <= 2:
        print("✓ Your caffeine intake before bed is minimal")
    else:
        print("⚠ Frequent caffeine consumption before bed may affect sleep quality")
    
    if avg_screen_time <= 3:
        print("✓ You're limiting screen exposure before bed")
    else:
        print("⚠ Frequent screen time before bed can disrupt your sleep")
    
    if avg_stress_level <= 4:
        print("✓ Your stress levels are relatively low")
    elif avg_stress_level <= 7:
        print("⚠ Moderate stress levels may be affecting your sleep")
    else:
        print("⚠ High stress levels are likely impacting your sleep quality")


def main():
    """Main program function"""
    # Collect sleep data
    total_sleep, sleep_times, total_caffeine, total_screen_time, total_stress = get_sleep_data()
    
    # Calculate averages
    days_in_week = 7
    avg_sleep_hours = total_sleep / days_in_week
    avg_sleep_diff = calculate_sleep_difference(sleep_times)
    avg_caffeine = total_caffeine  # Already a count for the week
    avg_screen_time = total_screen_time  # Already a count for the week
    avg_stress_level = total_stress / days_in_week
    
    # Analyze and provide recommendations
    analyze_sleep_quality(avg_sleep_diff, avg_sleep_hours, avg_caffeine, 
                         avg_screen_time, avg_stress_level)
    
    print("\n" + "=" * 60)
    print("Thank you for using the Sleep Tracker!")
    print("Sweet dreams and better sleep ahead! 😴")
    print("=" * 60)


if __name__ == "__main__":
    main()

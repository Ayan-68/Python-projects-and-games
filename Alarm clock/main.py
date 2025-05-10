import time
from datetime import datetime

def check_alarm_time(alarm_time):
    current_time = datetime.now().strftime("%H:%M")
    return current_time == alarm_time

def play_alarm():
    print("\nALARM! Time's up!")

def alarm_clock():
    alarm_time = input("Enter the alarm time (in HH:MM format, 24-hour): ")
    
    print(f"Alarm is set for {alarm_time}. Waiting...")
    
    while True:
        current_time = datetime.now().strftime("%H:%M")
        
        if current_time == alarm_time:
            play_alarm()
            break 
        
    
        time.sleep(30)

if __name__ == "__main__":
    alarm_clock()

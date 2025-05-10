import time 

a = "Hello! Welcome to your Stopwatch"
print("\n", a.center(90, '*'))


def stopwatch():
    hours = 0
    minutes = 0
    seconds = 0
    a = input("Enter '1' to start the clock or else press 'q' to quit: ")
    try:
        if int(a) == 1:
            while True:
                time.sleep(1)
                seconds += 1
                if seconds == 60:
                    seconds = 0
                    minutes += 1
                if minutes == 60:
                    minutes = 0
                    hours += 1
                print(f"{hours:02}:{minutes:02}:{seconds:02}")
        elif a.lower() == 'q':
            print("GoodBye")
    except Exception as e:
        print("Please Try Again", e)
        
stopwatch()

import time
import win32api

print("                 Hello There!                ")

a = input("In how much time do you want to be reminded everytime? write it minutes: ")
b = int(a)
c = 60 * b
print(c)

while True:
    old_hour = time.strftime("%H:%M:%S")
    print(f"Current time is: {old_hour}")


    time.sleep(c)

    new_time = time.strftime("%H:%M:%S")
    print(f"alarm popped at: {new_time} ")

    message = "DRINK YOUR WATER LAZYBUM!"
    title = "WATER!!!!"

    win32api.MessageBox(0, message, title, 100)

import time

my_timer = int(input("Enter the countdown time in seconds: "))

while my_timer:
    hrs, mins = divmod(my_timer, 3600)
    mins, secs = divmod(my_timer, 60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    my_timer -= 1

print("Time's up!") 
import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print("00:00 \nTime's Up!")

def main():
    total_seconds = int(input("Enter time in seconds for countdown timer: "))
    countdown(total_seconds)

if __name__ == '__main__':
    main()

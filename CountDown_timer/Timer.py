import time

def countdwon(t):
    while t: 
        mins, secs = divmod(t,60)
        timer = '{:02d}: {:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print('The time is Over.')

t = input('Input yor time is Second : ')
countdwon(int(t))
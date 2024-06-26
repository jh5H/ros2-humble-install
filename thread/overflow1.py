from time import sleep
from threading import Event, Thread

condition = Event()

def do_sth():
    print("truckin' ...")

def check_sth():
    while not condition.is_set():
        sleep(0.25)
        do_sth()  # Do something everytime the condition is not set.

    print("Condition met, ending.")


Thread(target=check_sth, args=()).start()
sleep(2)
condition.set()  # End while loop.

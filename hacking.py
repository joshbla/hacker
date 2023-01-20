import random as r
import string as s
import time


def print_random_hacker_text(going):
    hacker_text = ["Accessing the mainframe...", "Hacking the system...", "Overriding security protocols...", "Infiltrating network...", "Downloading classified data..."]
    exit_text = ["Obtained the desired information.", "Mission successful. Exiting system."]
    if going:
        print(r.choice(hacker_text))
    else:
        print(r.choice(exit_text))

def countDown():
    randNum = r.randint(10, 125)

    for i in range(randNum):
        print(randNum - i)
        time.sleep(.001)


# Set a random iterations
iterations = r.randint(1, 4)

for _ in range(iterations + 1):
    print()
    print_random_hacker_text(True)
    time.sleep(r.uniform(2.1, 3.5))
    
    # Get the current time in seconds
    start_time = time.time()
    seconds = r.uniform(0.01, 0.25)
    while time.time() - start_time < seconds:
        rChar1 = r.choice("ABCDEF" + s.digits)
        rChar2 = r.choice("ABCDEF" + s.digits)
        print(rChar1 + rChar2, end = " ")

print()
print_random_hacker_text(False)
time.sleep(r.uniform(2, 2.5))
countDown()
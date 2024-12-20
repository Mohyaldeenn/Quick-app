import os
import random
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def bus_with_name(name):
    bus = [
        "       ______________       ",
        "      |              |      ",
        "  .----|   " + f"{name:^8}" + "  |----.  ",
        " /_____|______________|_____\\ ",
        "  O    O            O    O   "
    ]
    return bus

def display_race(pos1, pos2, name1, name2):
    clear_screen()
    track_length = 180
    print(" " + "=" * (track_length + 14))
    print(f"{'BUS RACE'.center(track_length + 14)}")
    print(" " + "=" * (track_length + 14))
    
    bus1 = bus_with_name(name1)
    for line in bus1:
        print(" " * pos1 + line)
    print("-" * (track_length + 14))
    bus2 = bus_with_name(name2)
    for line in bus2:
        print(" " * pos2 + line)
    print("=" * (track_length + 14))

name1 = "Mohyaldeen"
name2 = "Ahmed     "
pos1 = 0
pos2 = 0
FINISH_LINE = 170

while pos1 < FINISH_LINE and pos2 < FINISH_LINE:
    display_race(pos1, pos2, name1, name2)
    pos1 += random.randint(2, 5)
    pos2 += random.randint(2, 5)
    time.sleep(0.3)
display_race(pos1, pos2, name1, name2)
if pos1 >= FINISH_LINE and pos2 >= FINISH_LINE:
    print("\n It's a draw! Both buses reached the finish line! ")
elif pos1 >= FINISH_LINE:
    print(f"\n Winner: {name1}'s car!")
else:
    print(f"\n Winner: {name2}'s car!")
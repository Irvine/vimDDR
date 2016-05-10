#! /usr/bin/python3

# For best results use source code pro
# Arrows
# "←..↑..↓..→"

import random
import getch
import time
import sys

score = 0
hearts = 3
fallback = False
giant = False

try:
    mode = sys.argv
except IndexError:
    mode = 'default'

if 'inf' in mode:
    hearts = 0
if 'fallback' in mode:
    fallback = True
elif 'giant' in mode:
    giant = True

left  = "←         "
down  = "   ↓      "
up    = "      ↑   "
right = "         →"
heart = " ❤"

if fallback:
    left  = "<           "
    down  = "   v        "
    up    = "      ^     "
    right = "         >  "
    heart = " <3"

if giant:
    left = "  /\n /\n \\\n  \\                      "
    down = "    \\      /\n     \\    /\n      \\  /\n       \\/                "
    up   = "                /\\\n               /  \\\n              /    \\\n             /      \\    "
    right= "                      \\\n                       \\\n                       /\n                      /  "
    heart = "<3 "

start = time.time()
def ddr(dirn):
    if dirn == 'h':
        print(left + gethearts(hearts))
    elif dirn == 'j':
        print(down + gethearts(hearts))
    elif dirn == 'k':
        print(up + gethearts(hearts))
    elif dirn == 'l':
        print(right + gethearts(hearts))

def gethearts(num):
    hc = ""
    while num > 0:
        hc = hc + heart
        num = num - 1
    return hc

while True:
    direction = random.choice(['h','j','k','l'])
    ddr(direction)
    char = getch.getch()
    if char == 'q':
        break
    elif char != direction:
        hearts = hearts - 1
        if hearts == 0:
            break
    else:
        score = score + 1
end = time.time()
time = round(end - start, 2)
print("Time : ", str(time)+"s")
print("Score: ", score)
print("Speed: ", round(score/time,2))

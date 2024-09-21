# TEST FILE

import curses
import random

stdscr = curses.initscr()


stdscr.addstr(0,0, chr(434))

size = 30
ran = range(size)
val = []
for i in ran:
	val.append(chr(random.randrange(1,100000)))

val = "".join(val)
print(val)

stdscr.addstr(2,0, val)

stdscr.refresh()

while 1:
	None

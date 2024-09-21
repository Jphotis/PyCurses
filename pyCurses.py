import curses
import random



# Initializes screen
stdscr = curses.initscr()


# Creates colors
""" List of the 8 colors:
0: COLOR_BLACK
1: COLOR_RED
2: COLOR_GREEN
3: COLOR_YELLOW
4: COLOR_BLUE
5: COLOR_MAGENTA
6: COLOR_CYAN
7: COLOR_WHITE
"""
curses.start_color()
# The standard color
curses.init_pair(100, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Extra colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_YELLOW)
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLUE)
curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_RED)

curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLACK)



# Waits for user to press any key. Detects key presses
# stdscr.getch()

# Adds stuff to the screen
val = 500
ran = range(val)
unicodeVals = []
while 1:
	for j in ran:
		for i in ran:
			# The try statements prevent the program from crashing when something tries to get printed off screen.
			try:	
				stdscr.addstr((i% 30 + j) % 43, j % 100, "This string gets printed at position (0, 0)")
			except:
				None
			
			if not i % 20:
				try:
					# Sets the color of the next text that will appear on the screen and where.
					stdscr.move(random.randrange(0,40), random.randrange(0,150))
				except:
					None
				try:
					stdscr.addstr("#", curses.color_pair(9))
				except:
					None
				if not i % 100:
					try:
						stdscr.addstr("Hello, world!", curses.color_pair(random.randrange(1,9)))
					except:
						None


			# Doing some unicode magic. Indents are as intended.
			if not i % 7:
				unicodeVals.append(chr(random.randrange(1,100000)))
		if not j % 5:
			lst = unicodeVals
			unicodeVals = "".join(lst)
			try:
				stdscr.addstr(unicodeVals, curses.color_pair(random.randrange(1,9)))
			except:
				None
			unicodeVals = []

		# Reprints the screen and waits 50 milliseconds.
		stdscr.refresh()
		curses.napms(50)		

	# Clears the screen
	stdscr.clear()
	stdscr.refresh()

# Displays screen every time this command is run
stdscr.refresh()





# Keep screen up for 2000 millisectionsd"
curses.napms(2000)





#curses.napms(10000)

# End screen
curses.endwin()



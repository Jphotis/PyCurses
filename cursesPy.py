import curses

# Initializes screen
screen = curses.initscr()





val = 500
ran = range(val)

while 1:
	for j in ran:
		for i in ran:
			screen.addstr((i% 30 + j) % 43, j % 100, "This string gets printed at position (0, 0)")
	
		screen.refresh()
		curses.napms(50)		


# Displays screen
screen.refresh()





# Keep screen up for 2000 millisectionsd"
curses.napms(2000)





#curses.napms(10000)

# End screen
# curses.endwin()



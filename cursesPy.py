import curses

# Initializes screen
screen = curses.initscr()





val = 50
ran = range(val)
for j in ran:
	for i in ran:
		screen.addstr(i% 30 + j, j % 30, "This string gets printed at position (0, 0)")
	
	screen.refresh()
	curses.napms(50)		


# Displays screen
screen.refresh()





# Keep screen up for 2000 millisectionsd"
curses.napms(2000)





#curses.napms(10000)

# End screen
# curses.endwin()



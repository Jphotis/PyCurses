import curses
import random



# Initializes screen
stdscr = curses.initscr()




# Adds stuff to the screen
val = 500
ran = range(val)

while 1:
	for j in ran:
		for i in ran:
			stdscr.addstr((i% 30 + j) % 43, j % 100, "This string gets printed at position (0, 0)")
			
			if not i % 20:
				stdscr.addstr(random.randrange(0,40),random.randrange(0,100), "#")	

				curses.start_color()
				curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

				stdscr.addstr("Hello, world!", curses.color_pair(1))
				stdscr.getch()

		stdscr.refresh()
		curses.napms(50)		



# Displays screen every time this command is run
stdscr.refresh()





# Keep screen up for 2000 millisectionsd"
curses.napms(2000)





#curses.napms(10000)

# End screen
curses.endwin()



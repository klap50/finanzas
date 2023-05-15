import curses

try:
    # Intenta inicializar la biblioteca curses
    curses.initscr()
    print("La biblioteca curses está instalada correctamente.")
except ImportError:
    print("La biblioteca curses no está instalada.")
finally:
    # Restaura el estado original de la terminal
    curses.endwin()

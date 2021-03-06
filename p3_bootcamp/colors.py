import termcolor
import pyfiglet

txt = termcolor.colored("Hi There!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(txt)


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "magenta"

    ascii_art = pyfiglet.figlet_format(msg)
    colored_ascii = termcolor.colored(ascii_art, color=color)
    print(colored_ascii)


msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)

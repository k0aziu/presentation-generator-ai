from colorama import Fore

def initialize():

    topic = input(Fore.CYAN + "\n1. " + Fore.WHITE + "What is the presentation about? ")

    slides = int(input(Fore.CYAN + "\n2. " + Fore.WHITE + "How many slides would you like for the presentation? "))

    return(str(topic), int(slides))
import introduction
import gpt_api
import choice

from colorama import Fore

global chat
chat = []

introduction.initialize()

topic, slides = choice.initialize()

print(gpt_api.ask_ai("Create a presentation outline for me, specifically " + str(slides) + " slides, each with its own topic, the main theme of the presentation is " + str(topic) + "." +
"""

The list should look like this:

Topic of the first slide.
Topic of the second slide.
Topic of the third slide.
Topic of the fourth slide.
Topic of the fifth slide.
...""", chat))

for slides in range(slides):

    question = "Write the content of slide number " + str(slides) + ". Incorporate a concise and informative content for slide 1, consisting of 3 to 5 sentences. If you want to add a note, write #note 'note'."

    print(Fore.GREEN + """\n\n  ___ _ _    _
 / __| (_)__| |___
 \\__ \\ | / _` / -_)\t""" + str(slides + 1) + """
 |___/_|_\\__,_\\___|
                   """ + Fore.WHITE + "\n\n")

    print(gpt_api.ask_ai(question, chat))

print(Fore.RED + """___________ _______  ________ ._.
\\_   _____/ \\      \\ \\______ \\| |
 |    __)_  /   |   \\ |    |  \\ |
 |        \\/    |    \\|    `   \\|
/_______  /\\____|__  /_______  /_
        \\/         \\/        \\/\\/""" + Fore.WHITE)
import sys
import os

BASE_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

from message_formatter import star_border, emoji_wrap

def format_message(message):
    return message

if __name__ == "__main__":
    print(star_border(format_message)("Hello from my decorator project!"))
    print(emoji_wrap(format_message)("Decorators are fun!"))
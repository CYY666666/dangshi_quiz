import re

pattern = re.compile('\[.*\]')

def get_message(full_message):
    return pattern.search(full_message).group()

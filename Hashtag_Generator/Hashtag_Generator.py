import re
import string


def generate_hashtag(s):
    nospaces = re.sub(r'\s','', string.capwords(s)) # Capitalize every letter beginning of a word or letter
    return False if len('#'+nospaces)>=140 or len(nospaces)<1 else '#'+nospaces
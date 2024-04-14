import re
import string
import random
from .constants import MATCH_URL


def get_random_string(length=6):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def is_valid_custom_id(custom_id):
    return bool(re.match(MATCH_URL, custom_id))

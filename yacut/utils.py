import string
import random

from .constants import DEFAULT_RANDOM_LEN_URL
from .models import URLMap


def get_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def get_random_url(length=DEFAULT_RANDOM_LEN_URL):
    random_string = get_random_string(length)
    while URLMap.is_short_exists(random_string):
        random_string = get_random_string(length)
    return random_string

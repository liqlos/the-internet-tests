import string, random


def random_string(size=8, chars=string.ascii_letters + string.digits):
    return "".join(random.choices(chars, k=size))

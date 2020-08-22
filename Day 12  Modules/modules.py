import random


def random_user_id():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = ''
    for i in range(6):
        res += random.choice(s)
    return res


def user_id_gen_by_user():
    n = int(input("Enter n : "))
    t = int(input("Enter t : "))
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(t):
        res = ''
        for j in range(n):
            res += random.choice(s)
        print(res)


def rgb_color_gen():
    r = random.randint(0, 256)
    b = random.randint(0, 256)
    g = random.randint(0, 256)
    return f"rgb({r},{b},{g})"


def list_of_hexa_colors():
    n = random.randint(0, 10)
    s = "0123456789abcdef"
    lst = []
    for i in range(n):
        res = '#'
        for j in range(6):
            res += random.choice(s)
        lst.append(res)
    return lst


def list_of_rgb_colors():
    n = random.randint(0, 10)
    lst = []
    for i in range(n):
        r = random.randint(0, 256)
        b = random.randint(0, 256)
        g = random.randint(0, 256)
        lst.append(f"rgb({r},{b},{g})")
    return lst


def generate_colors(type, n):
    if type == 'hexa':
        s = "0123456789abcdef"
        lst = []
        for i in range(n):
            res = '#'
            for j in range(6):
                res += random.choice(s)
            lst.append(res)
        print(lst)
    elif type == 'rgb':
        lst = []
        for i in range(n):
            r = random.randint(0, 256)
            b = random.randint(0, 256)
            g = random.randint(0, 256)
            lst.append(f"rgb({r},{b},{g})")
        print(lst)
    else:
        print("Enter type correctly")


def shuffle_list(lst):
    random.shuffle(lst)
    return lst


def seven_random():
    s = set()
    lst = []
    while True:
        if len(s) == 7:
            lst = s
            return lst
        n = random.randint(0, 10)
        s.add(n)

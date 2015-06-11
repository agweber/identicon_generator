#!/usr/local/bin/python3

# Author: Anthony Weber (weberag@gmail.com)
# Date Created: 2015-06-10
# Description: This is an identifying icon generator, shortened to identicon. It was made in vision of the
#   github identicons (see https://github.com/blog/1586-identicons), but with a little more freedom and
#   variation.

import random

def generate_symmetric_identicon(fill="X", empty=" ", height=10, width=10):
    half_width = int((width + 1) / 2)
    identicon = [[fill if random.randint(0, 1) == 0 else empty for w in range(half_width)] for h in range(height)]
    output = ""
    for h in range(height):
        for w in range(half_width):
            output += identicon[h][w]
        for w in reversed(range(half_width if width % 2 == 0 else half_width - 1)):
            output += identicon[h][w]
        output += "\n"
    return output

def generate_connected_identicon(fill="X", empty=" ", height=10, width=9, fillpercent=0.4):
    half_width = int((width + 1) / 2)  # +1 to round up (e.g. 9 width = 5 half_width)
    painted = 0
    max_painted = height * half_width * fillpercent
    adjacent = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]
    # initialize a blank identicon
    identicon = [[empty for w in range(half_width)] for h in range(height)]
    # 'paint' a single cell and add it to the stack
    y, x = random.randint(0, height - 1), random.randint(0, half_width - 1)
    lst = [(y, x)]
    while lst:
        # Take the first element off the list
        y, x = lst.pop()
        # Determine if we should paint it
        if painted <= max_painted:
            identicon[y][x] = fill
            painted += 1
            # Find all available neighbors and add them to the list (in a random order)
            # shuffle our adjacent positions table
            random.shuffle(adjacent)
            for pos_y, pos_x in adjacent:
                tmp_y, tmp_x = y + pos_y, x + pos_x
                if 0 <= tmp_x < half_width:
                    if 0 <= tmp_y < height:
                        # Make sure we haven't already painted it
                        if identicon[tmp_y][tmp_x] is not fill:
                            lst.append((tmp_y, tmp_x))
    # generate the string output
    output = ""
    for h in range(height):
        for w in range(half_width):
            output += identicon[h][w]
        # now add a mirror image, accounting for odd widths
        for w in reversed(range(half_width if width % 2 == 0 else half_width - 1)):
            output += identicon[h][w]
        output += "\n"
    return output

def generate_connected_identicon_2(fill="X", empty=" ", height=10, width=9, fillpercent=0.4, spacing=1.5):
    half_width = int((width + 1) / 2)  # +1 to round up (e.g. 9 width = 5 half_width)
    painted = 0
    max_painted = height * half_width * fillpercent
    adjacent = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]
    # initialize a blank identicon
    identicon = [[empty for w in range(half_width)] for h in range(height)]
    # 'paint' a single cell and add it to the stack
    y, x = random.randint(0, height - 1), random.randint(0, half_width - 1)
    lst = [(y, x)]
    while lst:
        # Take the first element off the list
        y, x = lst.pop()
        # Determine if we should paint it
        if painted <= max_painted:
            # Find all available neighbors and add them to lists
            # (first shuffle our adjacent positions table so we get a random order)
            random.shuffle(adjacent)
            filled_adjacent = 0
            empty_adjacent = []
            for pos_y, pos_x in adjacent:
                tmp_y, tmp_x = y + pos_y, x + pos_x
                # only check valid points
                if 0 <= tmp_x < half_width:
                    if 0 <= tmp_y < height:
                        # Make sure we haven't already painted it
                        if identicon[tmp_y][tmp_x] is not fill:
                            empty_adjacent.append((tmp_y, tmp_x))
                        else:
                            filled_adjacent += 1
            # decide if we want to fill this cell
            ratio = (len(empty_adjacent) / filled_adjacent) if filled_adjacent > 0 else 8  # avoid division by 0
            if ratio >= spacing:
                identicon[y][x] = fill
                painted += 1
                # if we do fill it, append empty cells to our search list
                lst.extend(empty_adjacent)

    # generate the string output
    output = ""
    for h in range(height):
        for w in range(half_width):
            output += identicon[h][w]
        # now add a mirror image, accounting for odd widths
        for w in reversed(range(half_width if width % 2 == 0 else half_width - 1)):
            output += identicon[h][w]
        output += "\n"
    return output

print("\nVertically symmetric random")
print(generate_symmetric_identicon("[]", "  ", 14, 7))
print("\n'Connected symmetric'")
print(generate_connected_identicon("[]", "  "))
print("\n'Connected symmetric with spacing'")
print(generate_connected_identicon_2("[]", "  "))
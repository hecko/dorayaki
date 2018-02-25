#!/usr/bin/env python3

from pprint import pprint

# zakladna definicia
flour = 75
sugar = 30
egg = 1
bp = 4
milk = 90
pieces = 7


def measures(eggs):
    out = {}
    out['eggs_no'] = eggs
    out['flour_g'] = flour * eggs
    out['sugar_g'] = sugar * eggs
    out['baking_powder_g'] = bp * eggs
    out['milk_g'] = milk * eggs
    return out

for eggs in range(1, 4):
    print("Using {} eggs means using:".format(eggs))
    pprint(measures(eggs))
    print("Estimated number of cakes when using 0.04l measure: {}".format(eggs * pieces))
    print("=-=-=-=-=-=-=-=-")

#!/usr/bin/env python3

from pprint import pprint

# definitions
flour = 75
sugar = 30
bp = 4
milk = 90
pieces = 7


def measures(eggs):
    out = {}
    out["eggs_no"] = eggs
    out["flour_g"] = flour * eggs
    out["sugar_g"] = sugar * eggs
    out["baking_powder_g"] = bp * eggs
    out["milk_g"] = milk * eggs
    return out


if __name__ == "__main__":
    for eggs in range(1, 4):
        print("Using {} eggs (cca 50g is weight of the egg) means using:".format(eggs))
        pprint(measures(eggs))
        print(
            "Estimated number of cakes when using 0.04l of batter per cake: {}".format(
                eggs * pieces
            )
        )
        print("=-=-=-=-=-=-=-=-")

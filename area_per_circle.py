#!/usr/bin/env python3

# Created by: Zak Goneau
# Created on: Sep. 22, 2023
# This program calculates the area and circumference of a circle with a radius of 6.7cm.

import math


def main():
    print("For a circle with a radius")
    print("of 6.7cm:")
    print("")
    print("Area= {:.2f}cm^2".format(math.pi * 6.7**2))
    print("Circumference= {:.2f}cm".format(2 * math.pi * 6.7))


if __name__ == "__main__":
    main()

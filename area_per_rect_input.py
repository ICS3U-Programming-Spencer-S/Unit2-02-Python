#!/usr/bin/env python3
# Created by: Spencer.Scarlett
# Created on: Sept 25, 2022
# This is a program for calculating the area and perimeter of a rectangle but with user input and in Python
import math


def main():
    # input
    print("This is to calculate the area and perimeter of a rectangle")
    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area = {} cm^2".format(area))
    print("Perimeter = {} cm".format(perimeter))


if __name__ == "__main__":
    main()

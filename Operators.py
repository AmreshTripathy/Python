#!/bin/python3

import math
import os
import random
import re
import sys

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())
        
tip = (meal_cost * (tip_percent / 100 ))

tax = (meal_cost * (tax_percent / 100))

totalCost = (meal_cost + tip + tax)

x = round(totalCost)

print(x)

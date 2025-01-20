#!/usr/bin/python

import pdftotext
import sys

#x = input('File to read: ')
x = sys.argv[1]

with open(x, "rb") as f:
    pdf = pdftotext.PDF(f)

#print(len(pdf))

for page in pdf:
    print(page)

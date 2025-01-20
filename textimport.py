#!/usr/bin/python

import pdftotext
import sys

x = sys.argv[1]

with open(x, "rb") as f:
    pdf = pdftotext.PDF(f)

for page in pdf:
    print(page)

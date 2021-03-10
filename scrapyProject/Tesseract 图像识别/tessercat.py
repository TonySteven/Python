#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/10/21 11:01
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : tessercat.py

import pytesseract
from PIL import Image

image = Image.open('test.png')
text = pytesseract.image_to_string(image)
print(text)

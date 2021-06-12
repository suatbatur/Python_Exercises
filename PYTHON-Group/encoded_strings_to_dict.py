# -*- coding: utf-8 -*-
"""encoded_strings_to_dict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pG0M0ETaJJmWU76RiGNnzzm_zKisL043
"""

Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}
parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}
parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}

def parse_code(s):
  l=s.replace("0"," ").split()
  print(l)
  return {"first_name":l[0], "last_name":l[1], "id":l[2]}

parse_code("John000Doe000123")

def dict_maker(sample):
  values = [i for i in sample.split("0") if i!=""]
  keys = ["first_name", "last_name", "id"]
  my_dict = dict(zip(keys,values))
  print(my_dict)
dict_maker("John000Doe000123")
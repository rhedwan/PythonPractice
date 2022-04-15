from pydoc import describe
from unicodedata import name


name = "Bola"
print("Hello World,", name)

descr = "Crypto money from Jack Benson"
print(descr.find("Crypto", 1))

concat_string = lambda a,b,c : a[0] + b[0] + c[0]
print(concat_string("Jack","Elon","Bretha" ).upper())
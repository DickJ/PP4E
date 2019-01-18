def blah(b):
    a *= 3

global a
a = 2
blah(a)
print(a)

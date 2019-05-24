mystuff1 = {'apple': "I AM APPLES!"}
print(mystuff1['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff1['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, its just a variable

class MyStuff(object):

    def _init_(self):
        self.tangerine = "And now a thousand years between."

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# dict style
mystuff1['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

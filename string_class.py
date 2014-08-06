class StringClass(object):
    """ Class to get and print a string """
    def __init__(self):
        super(StringClass, self).__init__()
        self.arg = ""

    def getString(self):
        self.arg = raw_input("Enter your string: ")

    def printString(self):
        print "You entered:", self.arg

str = StringClass()
str.getString()
str.printString()

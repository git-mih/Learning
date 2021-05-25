class Spam:
    numInstances = 0   # class level variable
    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances created: {0}'.format(Spam.numInstances))

a = Spam()
b = Spam()
c = Spam()
d = Spam()

a.printNumInstances()
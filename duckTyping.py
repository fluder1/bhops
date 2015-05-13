class Human:
    def quack(self):
        print "What"
        
class Duck:
    def quack(self):
        print "Quack"

class Snake:
    def quack(self):
        print "Hsssssss"

bob = Human()
browntail = Duck()
diamondhead = Snake()
bob.quack()
browntail.quack()
diamondhead.quack()

    
# add your code from task 1 between the lines
#---------------------------------------------------------------------------

#creating a class
class Things:
    pass
#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Animate(Things):
    # example of a class function
    def exist(self):
        print('Cogito ergo sum')

class Sidewalks(Inanimate):
	pass

class Animals(Animate):
	def eat(self):
		print('I can eat')
	def move(self):
		print('I can move')
	def love(self):
		print('I can love')


class Mammals(Animals):
	def feed_milk_to_cubs(self):
		print('we can feed the milk of our cubs')
  

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('I can eat leaves from trees')
    

#creating an object of a given class
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

infusorium = Animate()
infusorium.exist()

#---------------------------------------------------------------------------

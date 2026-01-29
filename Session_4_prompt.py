class animal:
	def __init__(self, length_of_arms: float, length_of_legs: float, number_of_eyes: int, tail: bool, is_it_furry: bool):
		self.length_of_arms = length_of_arms
		self.length_of_legs = length_of_legs
		self.number_of_eyes = number_of_eyes
		self.tail = tail
		self.is_it_furry = is_it_furry
	def __str__(self):
		return(
			f"{self.length_of_arms}m "
			f"{self.length_of_legs}m "
			f"{self.number_of_eyes} "
			f"{self.tail} "
			f"{self.is_it_furry} "
		)	
Secretary_Bird = animal( 2.0, 0.31, 2, 1, 1)
print(Secretary_Bird)
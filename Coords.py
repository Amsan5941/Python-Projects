class Point:  #This code creates the "Point" class
	def __init__(self, x, y):  # Constructor for point class.
		self.x = x
		self.y = y

	def get_x(self):  # Returns the x-coordinate value.
		return self.x

	def get_y(self):  # Returns the x-coordinate value.
		return self.y

	def __repr__(
	    self
	):  # This function is executed when an object is printed and returns the coordinates of one point of the line.
		return f"The coordinates for one point of the line are {self.x} and {self.y}"


class Line:  #This code creates the "Line" class
	def __init__(self, point1, point2):  # Constructor for line class.
		self.point1 = point1  #This gets the value of point1 from the client code and stores it in a variable in the "line" class
		self.point2 = point2  #This gets the value of point2 from the client code and stores it in a variable in the "line" class

	def length(
	    self
	):  #This function uses the 4 coordinates to find the length of the line

		#The following lines of code gets the value from the Point class and stores the value in a new condensed variable
		x1 = self.point1.get_x()
		y1 = self.point1.get_y()
		x2 = self.point2.get_x()
		y2 = self.point2.get_y()

		line_length = 0.5 * (
		    (x2 - x1)**2 + (y2 - y1)**2
		)  #This finds the length of the code using the length formula of a line
		return line_length  #Returns the length of the line when the function is called

	def __eq__(self, line2):  #This function compares the length of the 2 lines
		if (self.length() == line2.length()):
			return True
		else:
			return False

	def __repr__(
	    self
	):  #This function gets executed when an object is printed and returns the length of the line.
		return f"The length of the line is {self.length()}"  # This function is executed when an object is printed.


#The following lines of code are in the client code and are variables for each point of the 2 lines. It uses the Point code created above
point1 = Point(2, 4)
point2 = Point(5, 7)
point3 = Point(3, 6)
point4 = Point(8, 5)

#The following 2 lines of code  are used in the Line class and stores 2 points into 1 variable to create a line variable
line1 = Line(point1, point2)
line2 = Line(point3, point4)

if (line1 == line2
    ):  #This if statement checks to see if both lines have the same length
	print(
	    'The lines have the same length!'
	)  #If the condition is true, the following print statement is outputted

#The following lines of code prints the 2 points and length of each line
print(point1)
print(point2)
print(line1)
print('\n')
print(point3)
print(point4)
print(line2)

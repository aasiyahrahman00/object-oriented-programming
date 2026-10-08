class Point:
    def __init__(self, x, y):
        # Store x and y coordanites of the point
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Two point objects considered equal if they have the same x coordinate and same y coordiante 
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

class Line:
    def __eq__(self, other):
        # Ensures object being compared is a Line object, if not the two objects cannot be equal
        if not isinstance(other, Line):
            return False

        # Check if both points match in same order e.g. Line(A, B) == Line(A, B)
        same_order = self.point1 == other.point1 and self.point2 == other.point2
        # Check if both points match in reverse order e.g. Line(A, B) == Line(B, A)
        reverse_order = self.point1 == other.point2 and self.point2 == other.point1

        # Returns True if either comparison matches, lines are equal when they contain the same two point objects regardless of order.
        return same_order or reverse_order


    def midpoint(self):
        # Calculate x-coordinate halfway between two endpoints
        mid_x = (self.point1.x + self.point2.x) / 2

        # Calulate y-coordinate halfway between two endpointa
        mid_y = (self.point1.y + self.point2.y) / 2

        # Return midpoint as new Point object
        return Point(mid_x, mid_y)


class Rectangle:
    def midpoint(self):
        # Calculate x-coordinate halfway across rectangle
        mid_x = self.corner.x + self.width / 2
        # Calculate y-coordinate halfway through rectangle height
        mid.y = self.corner.y + self.height / 2
 
        # Return centre of rectangle as new Point object
        return Point(mid_x, mid_y)

    def make_cross(self):
        # Get four rectangle sides as Line objects
        lines = self.make_lines()

        # Find midpoint of each side
        midpoint_1 = lines[0].midpoint()
        midpoint_2 = lines[1].midpoint()
        midpoint_3 = lines[2].midpoint()
        midpoint_4 = lines[3].midpoint()

        # Connect opposite side midpoints to form the cross
        crossline_1 = Line(midpoint_1, midpoint_2)
        crossline_2 = Line(midpoint_2, midpoint_4)

        # Return the two cross lines as a list
        return [crossline_1, crossline_2]

class Circle:
    def __init__(self, center, radius):
        # Store center of corcle as Point object
        self.center = center
        # Store radius of circle as number
        self.radius = radius

    def __str__(self):
        # Return a readable version of the Circle object
        return f"Cricle(center={self.center}, radius={self.radois})"

    def draw(self):
        # Lift the pen so the turtle can move without drawing a line
        penup()
 
        # Move to the bottom point of the circle. Turtle circles are drawn relative to the turtle's starting position, so we move down by the radius from the centre.
        goto(self.conter.x, self.center.y - self.radius)

        # Put the pen down so the circle is drawn
        pendown()
        
        # Draw the circle using the stored radius
        circle(self.radius)
import turtle

# Set up the turtle screen with a background color
turtle.Screen().bgcolor("Aqua")

# Create a turtle object named board
board = turtle.Turtle()

# First triangle for the star
board.forward(100)  # Draw the base of the triangle

board.left(120)  # Turn left by 120 degrees
board.forward(100)  # Draw the second side of the triangle

board.left(120)  # Turn left by 120 degrees
board.forward(100)  # Draw the third side of the triangle

# Move to the starting position for the second triangle
board.penup()  # Lift the pen to avoid drawing while moving
board.right(150)  # Turn right by 150 degrees
board.forward(50)  # Move forward by 50 units

# Second triangle for the star
board.pendown()  # Lower the pen to start drawing
board.right(90)  # Turn right by 90 degrees
board.forward(100)  # Draw the first side of the triangle

board.right(120)  # Turn right by 120 degrees
board.forward(100)  # Draw the second side of the triangle

board.right(120)  # Turn right by 120 degrees
board.forward(100)  # Draw the third side of the triangle

# Complete the drawing
turtle.done()

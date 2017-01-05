# Do not run.

# Drawing shapes
# w/o polymorphism
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
         a_shape.draw_circle()

# Drawing shapes
# with polymorphism
shapes = [tr1,
          sw1,
          cr1]
for a_shape in shapes:
    a_shape.draw()

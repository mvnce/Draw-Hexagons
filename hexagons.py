# Python turtle draw hexagons
# written by VincentMa
import turtle, math

turtle.speed('fastest')

turtle.left(90)

def get_num_hexagons():
    """ None parameters
        This function return an 'int' in 4,5,6, ... , 20 """
    num = int(input("Please enter a number of hexagons per row:"))
    return num
        
def get_color_choice():
    """ None parameters
        Return a Tk symbolic name """
    color1 = input("Please enter your 1st choice for colors to use:")
    color2 = input("Please enter your 2nd choice for colors to use:")
    return (color1,color2)

def draw_hexagons(x,y,side_len,pen,color):
    """ Parameters: x,y-coordinates
                    side_len
                    pen (turtle)
                    color
        return None (No return value) """
    pen.up()
    pen.goto(x,y)
    pen.down()

    pen.begin_fill()
    pen.color('black',color)
    pen.right(60)
    pen.forward(side_len)
    pen.right(60)
    pen.forward(side_len)
    pen.right(60)
    pen.forward(side_len)
    pen.right(60)
    pen.forward(side_len)
    pen.right(60)
    pen.forward(side_len)
    pen.right(60)
    pen.forward(side_len)
    pen.end_fill()

def main():
    hex_num = get_num_hexagons()
    hex_col = get_color_choice()

    hex_len = (600/hex_num)
    hex_side_len = ((hex_len/2)/math.sin(math.pi/3))

    initial_x = -300
    initial_y = -300 + 2*hex_side_len
    counter_line = 0
    counter_row = 0
    counter_error = 0

    while counter_row < hex_num:

        while counter_line < hex_num:

            if counter_line%2 == 0:
                draw_hexagons(initial_x,initial_y,hex_side_len,turtle,hex_col[0])
            else:
                draw_hexagons(initial_x,initial_y,hex_side_len,turtle,hex_col[1])
            initial_x += hex_len
            counter_line += 1
    
        initial_y += ((3/2)*hex_side_len)
        if counter_error%2 == 0:
            initial_x = -300 + (hex_len/2)
        else:
            initial_x = -300
        counter_row += 1
        counter_error += 1
        counter_line = 0

main()

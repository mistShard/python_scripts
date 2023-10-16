# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    interval = 50
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    #draw_grid(canvas, scene_width, scene_height, interval)
    
    sky_height = draw_sky(canvas, scene_height, scene_width)
    draw_ground(canvas, scene_width, sky_height)
    #draw_grid(canvas, scene_width, scene_height, interval)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):
    # draw vertical line
    label_y = 20
    for i in range(interval, width, interval):
        draw_line(canvas, i, 0, i, height, fill="red" )
        draw_text(canvas, i, label_y, str(i), fill="blue")


    # draw horizontal line
    label_x = 20
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill="blue")
        draw_text(canvas, label_x, y, str(y), fill="red")

    
def draw_sky(canvas, scene_height, scene_width):
    # a background for the sky
    a = (scene_height / 1.5)
    sky_height = round(scene_height - a)
    draw_rectangle(canvas, 0, (sky_height), scene_width, scene_height, outline="skyblue", fill="skyblue")
    # draw the sun
    draw_oval(canvas, 100, 350, 250, 500, fill="yellow", outline="yellow" )
    # draw clouds
    draw_clouds(canvas, cloud_end = 0)
    draw_bird(canvas, sky_height)
    # return this value in order to use it to determine the height of the\
    # ground.
    return sky_height

    
def draw_ground(canvas, scene_width, sky_height):
    draw_rectangle(canvas, 0, 0, scene_width, sky_height, fill="chocolate3", outline="saddlebrown")
    interval = 150
    for i in range(interval, scene_width, 200):    
    # Draw a pine tree.
        tree_center_x = i
        tree_bottom = 100
        tree_height = 200
        min_diam = 5
        max_diam = 10
        draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    draw_pebbles(canvas, sky_height, scene_width, max_diam, min_diam )

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height    
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_pebbles(canvas, sky_height, scene_width, max_diam, min_diam ):
    num_pebbles = 200
    for i in range(num_pebbles):
        x = random.randint(0, scene_width - max_diam)
        sh = int(sky_height / 2)
        y = random.randint(0, sh)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="saddlebrown", outline="gray12")

def draw_bird(canvas, sky_height, size = 20):
    bird_size = size
    height = bird_size / 2
    for i in range(0, int(sky_height / 40)):
        color = bird_color('seashell4', 'lightblue4', 'black')
        # make the black birds appear closer by increasing their size
        if color.lower() == 'black':
            bird_size = 30
            height = bird_size / 2

        center_x = random.randint(300, 450)
        draw_arc(canvas, center_x - size, center_x + height, center_x, center_x, outline = color)
        draw_arc(canvas, center_x, center_x, center_x + size, center_x + height, start = 90, outline = color)

def bird_color(color1, color2, color3):
    # randomly select a bird color
    color_box = [color1, color2, color3]
    color_index = random.randint(0, len(color_box) - 1)
    color = color_box[color_index]
    return color
    


def draw_clouds(canvas, cloud_end, outline = 'white', fill = 'white'):
        for i in range(4):
            if cloud_end > 500 or cloud_end <= 0:
                center = random.randint(100, 500)
            else:
                center = random.randint(100, cloud_end)
            x1 = center - 100
            x2 = center + 100
            y1 = center
            y2 = center + 100
            if center < 350:
                draw_oval(canvas, center - 40, center, center + 50, center + 50, outline = outline, fill = fill)
            else:
                draw_oval(canvas, x1, y1, x2, y2, fill = fill, outline = outline, width = 10)
# Call the main function so that
# this program will start executing.
main()
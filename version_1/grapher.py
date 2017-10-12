from PIL import Image

# For rounding
from math import log10, floor


def round_to(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


def plane_grapher(lB_2D_points, l_window_size, l_plane_size, i_iterations, run_number):
    i_x_pixel   = l_window_size[0]
    i_y_pixel   = l_window_size[1]

    d_x_min     = l_plane_size[0]
    d_y_min     = l_plane_size[1]
    d_x_size    = l_plane_size[2]
    d_y_size    = l_plane_size[3]

    significant_digits = 2

    # Create image
    img_path = "img/iter_loop/" + str(run_number) + ". (" + str(i_x_pixel) + "x" + str(i_y_pixel) + "), [" + str(round_to(d_x_min, significant_digits)) + "," + str(round_to(d_y_min, significant_digits)) + "] - [" + str(round_to(d_x_min+d_x_size, significant_digits)) + "," + str(d_y_min+d_y_size) + "], " + str(i_iterations) + "-iter.png"
    #img_path = "img/mep.png"
    img = Image.new('RGB', (i_x_pixel, i_y_pixel), (127, 127, 127))
    pixels = img.load()
    

    for x in range(i_x_pixel):
        for y in range(i_y_pixel):
            if(lB_2D_points[x][y]):
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)
    

    pixels = draw_axis(pixels, l_window_size, l_plane_size)

    #img.putdata(pixels)
    #print(pixels)
    img.save(img_path)
    print("Imagecreated:\t" + img_path)
    #img.show()


def draw_axis(pixels, l_window_size, l_plane_size):
    axis_color = (127, 127, 127)
    for x in range(l_window_size[0]):
        for y in range(l_window_size[1]):

            # x/y points
            x_point = coord_finder(
                l_window_size[0],
                x,
                l_plane_size[0],
                l_plane_size[0] + l_plane_size[2]
            )
            y_point = coord_finder(
                l_window_size[1],
                y,
                l_plane_size[1],
                l_plane_size[1] + l_plane_size[3]
            )

            # diffs
            diffX = abs(l_plane_size[2] / l_window_size[0])
            diffY = abs(l_plane_size[3] / l_window_size[1])

            # x_point
            if(l_window_size[0] % 2 == 0):  # Even
                if(x_point < 0+diffX and x_point > 0-diffX):    # x_point == 0
                    pixels[x, y] = axis_color
            else:   # Odd
                if(x_point < 0+diffX and x_point >= 0):         # x_point == 0
                    pixels[x, y] = axis_color
            
            # y_point
            if(l_window_size[1] % 2 == 0):  # Even
                if(y_point < 0+diffY and y_point > 0-diffY):    # y_point == 0
                    pixels[x, y] = axis_color
            else:   # Odd
                if(y_point < 0+diffY and y_point >= 0):         # y_point == 0
                    pixels[x, y] = axis_color
            #if((x_point < 0+diffX and x_point > 0-diffX) or (y_point < 0+diffY and y_point > 0-diffY)):
                #(l_window_size[0] / l_window_size[1]) * l_plane_size[0] == 0 or
                #(l_window_size[0] / l_window_size[1]) * l_plane_size[1] == 0):   # If x == 0 or y == 0
                
    return pixels


def coord_finder(i_pix, i_this_pix, d_min, d_max):
    pix_frac = i_this_pix / (i_pix -1)      # Pixel number 500 / total of 1000 pixels = 1/2.
    pos = d_min + pix_frac*(d_max - d_min)  # -2 + (1/2)(width of zoom 4) = -2 + 1/2*4 = 0.
    return pos

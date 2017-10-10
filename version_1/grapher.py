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
    img_path = "img/iter_loop/" + str(run_number) + ". (" + str(round_to(i_x_pixel, significant_digits)) + "x" + str(round_to(i_y_pixel, significant_digits)) + "), [" + str(round_to(d_x_min, significant_digits)) + "," + str(round_to(d_y_min, significant_digits)) + "] - [" + str(round_to(d_x_min+d_x_size, significant_digits)) + "," + str(d_y_min+d_y_size) + "], " + str(i_iterations) + "-iter.png"
    #img_path = "img/mep.png"
    img = Image.new('RGB', (i_x_pixel, i_y_pixel), (127, 127, 127))
    pixels = img.load()
    

    for x in range(i_x_pixel):
        for y in range(i_y_pixel):
            if(lB_2D_points[x][y]):
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)
    
    #img.putdata(pixels)
    #print(pixels)
    img.save(img_path)
    print("Imagecreated:\t" + img_path)
    #img.show()

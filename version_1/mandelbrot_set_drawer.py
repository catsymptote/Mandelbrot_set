import sys
import time

from version_1 import complex_maths
from version_1 import grapher



def mandelbrot_function(c_z, c_c):
    #c_sq_z  = complex_maths.complex_square(c_z)
    #output  = complex_maths.complex_add(c_sq_z, c_c)

    output = complex_maths.complex_add(
        complex_maths.complex_square(c_z),
        c_c
    )

    return output


def point_lister(l_window_size, l_plane_size, iterations):
    ##  Ignore maybe?
    ##  l_window_size is the pixel count
    ##      [i_x_pixel, i_y_pixel]
    ##  l_plane_size is the coord size of the represented field:
    ##      [x_start, y_start, x_size, y_size]
    ##  l_2D_plane is a 2D plane of a list of the real and imaginary parts of a complex number.
    ##  I.e. listX<listY<listComplex>>

    i_x_pixel   = l_window_size[0]
    i_y_pixel   = l_window_size[1]

    d_x_min     = l_plane_size[0]
    d_y_min     = l_plane_size[1]
    d_x_size    = l_plane_size[2]
    d_y_size    = l_plane_size[3]
    
    lB_2D_plane  = [] # 2D list of boolean values

    # Make list<list<bool>>
    for x1 in range(i_x_pixel):
        new = []
        for y1 in range(i_y_pixel):
            new.append(False)
        lB_2D_plane.append(new)

    trues = 0
    falses = 0

    
    print("i_x_pixel: " + str(i_x_pixel) + ",\ti_y_pixel: " + str(i_y_pixel))

    for y in range(i_y_pixel):
        for x in range(i_x_pixel):
            x_point = coord_finder(
                i_x_pixel,
                x,
                d_x_min,
                d_x_min + d_x_size
            )
            y_point = coord_finder(
                i_y_pixel,
                y,
                d_y_min,
                d_y_min + d_y_size
            )
            #print("x_point:\t" + str(x_point) + ",\t\ty_point:\t" + str(y_point))
            #print("x: " + str(x) + ",\ty:" + str(y))
            c_c = [x_point, y_point]
            c_z = c_c
            for i in range(iterations):
                #print(str(x) + ":" + str(y) + " :" + str(i) + " -> " + str(res))
                #c_z = complex_maths.complex_add(
                #    mandelbrot_function(c_z, c_c),  # z_n+1
                #    c_z                             # z_n
                #    #c_z,                            # z
                #    #mandelbrot_function(c_z, c_c)   # c
                #)   
                c_z = mandelbrot_function(c_z, c_c)

                if(c_z[0] > 2 or c_z[1] > 2):
                    break
            
            if(complex_maths.complex_length(c_z) >= 2):
                lB_2D_plane[x][y] = True
                trues += 1
            else:
                lB_2D_plane[x][y] = False
                falses += 1
            #print(res)
            #print("--")
            #print(complex_maths.complex_length(res))
        # print(y)   # Show how many rows are compelted (rudimentary progress bar)
        #sys.stdout.flush()
    #print("-----")
    #print("True: " + str(trues))
    #rint("False: " + str(falses))
    print("True/False ratio:\t" + str(trues / falses))
    return lB_2D_plane


def coord_finder(i_pix, i_this_pix, d_min, d_max):
    # Pixel number 500 / total of 1000 pixels = 1/2.
    # -2 + (1/2)(width of zoom 4) = -2 + 1/2*4 = 0.

    # Pixel 600/900 = 2/3
    # -2 + (2/3)(3) = 0

    # Pixel 300/900 = 1/3
    # -2 + (1/3)(3) = -1
    pix_frac = i_this_pix / (i_pix -1)      
    pos = d_min + pix_frac*(d_max - d_min)  
    return pos


# Test
"""
l_window_size = [2048, 2048]    # pixel image size
l_plane_size = [-2, -2, 4, 4]   # -2 and 4 up in x and y in the complex plane
b_mandel_list = point_lister(
    l_window_size,
    l_plane_size
)
grapher.plane_grapher(
    b_mandel_list,
    l_window_size,     
    l_plane_size
)
"""

# Tests
#print(complex_maths.complex_add([3, 4], [1, 7]))
#print(complex_maths.complex_square([3, 4]))
#print(complex_maths.complex_length([3, 4]))


## Change to decimals??

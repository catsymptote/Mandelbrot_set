from PIL import Image


def plane_grapher(lB_2D_points, l_window_size, l_plane_size):#, i_iterations):
    i_x_pixel   = l_window_size[0]
    i_y_pixel   = l_window_size[1]

    d_x_min     = l_plane_size[0]
    d_y_min     = l_plane_size[1]
    d_x_size    = l_plane_size[2]
    d_y_size    = l_plane_size[3]

    # Create image
    """
    img_path = "img/"
        + str(i_x_pixel) + "x" + str(i_y_pixel) + ", ["
        + str(d_x_min) + "," + str(d_y_min) + "] - ["
        + str(d_x_min+d_x_size) + "," + str(d_y_min+d_y_size) + "]"
        + str(i_iterations) + ".png"
    """
    img_path = "img/mep.png"
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
    #img.show()

from version_1 import mandelbrot_set_drawer
from version_1 import complex_maths
from version_1 import grapher



def create_mandelbrot_set(l_window_size, l_plane_size, i_iterations, run_number):
    b_mandel_list = mandelbrot_set_drawer.point_lister(
        l_window_size,
        l_plane_size,
        i_iterations
    )
    grapher.plane_grapher(
        b_mandel_list,
        l_window_size,     
        l_plane_size,
        i_iterations,
        run_number
    )



# The zoom level
zoom = 1.0

# -2 and 4 up in x and y in the complex plane
l_plane_size = [-2.0/zoom, -2.0/zoom, 4.0/zoom, 4.0/zoom]

# pixel image size
pix = 4096
l_window_size = [int(pix*(l_plane_size[2]/l_plane_size[3])), int(pix)]
# Ensuring single line width for axis.
if(l_window_size[0] %2 == 0):
    l_window_size[0] += 1
if(l_window_size[1] %2 == 0):
    l_window_size[1] += 1

# How many checks
i_iterations = 250


# How many loops. i_loop_count / i_loop_step amount of pictures will be generated
i_loop_count = 1

# How large steps
i_loop_step = 1

for i in range(i_loop_count):
    create_mandelbrot_set(l_window_size, l_plane_size, i_iterations, i+1)
    #i_iterations += i_loop_step
    print(l_plane_size)
    zoom *= 2.0
    l_plane_size = [-2.0/zoom, -2.0/zoom, 4.0/zoom, 4.0/zoom]

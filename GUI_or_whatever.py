from version_1 import mandelbrot_set_drawer
from version_1 import complex_maths
from version_1 import grapher



l_window_size = [4096, 4096]    # pixel image size
l_plane_size = [-2, -2, 4, 4]   # -2 and 4 up in x and y in the complex plane
runs = 500                      # How many checks

b_mandel_list = mandelbrot_set_drawer.point_lister(
    l_window_size,
    l_plane_size,
    runs
)
grapher.plane_grapher(
    b_mandel_list,
    l_window_size,     
    l_plane_size
)

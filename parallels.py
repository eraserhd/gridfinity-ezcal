from build123d import *
from gridfinity_build123d import *
import math

# Defaults are for this set:
# https://littlemachineshop.com/products/product_view.php?ProductID=1893
parallel_pair_count = 10
parallel_width = 3.0 * 25.4
parallel_thickness = 1.0/8.0 * 25.4
shortest_parallel_height = 1/2 * 25.4
tallest_parallel_height = (1 + 5/8) * 25.4

slot_clearance = 0.01 * 25.4
slot_width = parallel_width + 2 * slot_clearance
slot_thickness = parallel_thickness * 2 + 2 * slot_clearance
minimum_wall_size = 1.5

slot_z = 5
percent_exposed = 0.33
shortest_height = percent_exposed * shortest_parallel_height + slot_z
tallest_height = percent_exposed * tallest_parallel_height + slot_z

# Compute the minimum number of grids we need
grid_x = math.ceil((slot_width + 2*minimum_wall_size)/42.0)
grid_y = math.ceil((parallel_pair_count * slot_thickness + (parallel_pair_count + 1) * minimum_wall_size)/42.0)

slot_wall_thickness = (grid_y*42.0 - parallel_pair_count * slot_thickness) / (parallel_pair_count + 1)
offset_y = slot_thickness + slot_wall_thickness
first_slot_y = -grid_y*42.0/2.0 + slot_wall_thickness + slot_thickness/2.0

with BuildPart() as bin:
    Bin(
        BaseEqual(grid_x=grid_x, grid_y=grid_y),
        height=tallest_height - 3.0,
    )
    with Locations([
        (0, first_slot_y + offset_y*n, slot_z)
        for n in range(parallel_pair_count)
    ]):
        Box(
            length=slot_width,
            width=slot_thickness,
            height=tallest_parallel_height,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
            mode=Mode.SUBTRACT,
        )

with BuildPart() as top_cutaway:
    with BuildSketch(Plane.YZ):
        with BuildLine():
            front = -grid_y*42.0/2.0
            back = +grid_y*42.0/2.0
            top = tallest_height + 1
            s0 = Line((front, shortest_height), (front, top))
            s1 = Line(s0 @ 1, (back, top))
            s2 = Line(s1 @ 1, (back, tallest_height))
            s3 = Line(s2 @ 1, s0 @ 0)
        make_face()
    extrude(amount=grid_x * 42.0 / 2.0, both=True)

(bin.part - top_cutaway.part).export_stl("parallels.stl")

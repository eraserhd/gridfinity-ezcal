from build123d import *
from gridfinity_build123d import *

# |bb -e '(printf "%.02f" (double (* (load-string (slurp *in*)) 25.4)))'<ret>

#EZCal
with BuildPart() as cutout:
    with BuildSketch():
        with BuildLine():
            caliper_length = 235
            scale_width = 16
            scale_bottom_height = 2.45

            s0 = Line((235.97, 20.32),(235.97, 20.32 + scale_width))
            s1 = Line(s0 @ 1,(94.75, 20.32 + scale_width))
            s2 = Bezier(s1 @ 1,(94.75, 38.61),(98.81, 46.23),(91.95, 49.02))
            s3 = Bezier(s2 @ 1,(84.84, 51.82),(81.79, 45.47),(81.79, 45.47))
            s4 = Line(s3 @ 1,(72.65, 50.80))
            s5 = Line(s4 @ 1,(55.63, 43.69))
            s6 = Line(s5 @ 1,(29.47, 43.69))
            s7 = Line(s6 @ 1,(23.12, 70.61))
            s8 = Line(s7 @ 1,(15.50, 77.47))
            s9 = Line(s8 @ 1,(9.15, 70.61))
            s10 = Line(s9 @ 1,(1.02, 42.16))
            s11 = Line(s10 @ 1,(0.00, 18.03))
            s12 = Line(s11 @ 1,(4.32, 3.81))
            s13 = Bezier(s12 @ 1,(5.08, 2.54),(6.35, 1.27),(7.88, 0.25))
            s14 = Bezier(s13 @ 1,(9.40, 1.52),(10.42, 2.79),(11.94, 4.57))
            s15 = Line(s14 @ 1,(14.74, 13.72))
            s16 = Line(s15 @ 1,(39.63, 14.22))
            s17 = Line(s16 @ 1,(39.63, 6.10))
            s18 = Line(s17 @ 1,(48.52, 6.10))
            s19 = Line(s18 @ 1,(48.77, 13.97))
            s20 = Line(s19 @ 1,(59.69, 13.72))
            s21 = Bezier(s20 @ 1,(65.03, 10.92),(70.62, 10.92),(76.71, 13.72))
            s22 = Bezier(s21 @ 1,(82.55, 12.70),(84.08, 13.72),(83.32, 20.57))
            s23 = Line(s22 @ 1, s0 @ 0)
        make_face()
    extrude(amount=5, dir=(0,0,-1))

cutout.part.export_stl("cutout.stl")

#calipers_bin = gf.Bin(gf.BaseEqual(2, 6), height_in_units=4)
#bd.export_stl(calipers_bin, "calipers_bin.stl")

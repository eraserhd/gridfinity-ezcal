from build123d import *
from gridfinity_build123d import *

# |bb -e '(printf "%.02f" (double (* (load-string (slurp *in*)) 25.4)))'<ret>

#EZCal
with BuildPart() as cutout:
    with BuildSketch():
        with BuildLine():
            s0 = Line((236.22, 20.32),(236.22, 38.10))
            s1 = Line(s0 @ 1,(95.00, 38.61))
            s2 = Bezier(s1 @ 1,(95.00, 38.61),(99.06, 46.23),(92.20, 49.02))
            s3 = Bezier(s2 @ 1,(85.09, 51.82),(82.04, 45.47),(82.04, 45.47))
            s4 = Line(s3 @ 1,(72.90, 50.80))
            s5 = Line(s4 @ 1,(55.88, 43.69))
            s6 = Line(s5 @ 1,(29.72, 43.69))
            s7 = Line(s6 @ 1,(23.37, 70.61))
            s8 = Line(s7 @ 1,(15.75, 77.47))
            s9 = Line(s8 @ 1,(9.40, 70.61))
            s10 = Line(s9 @ 1,(1.27, 42.16))
            s11 = Line(s10 @ 1,(0.25, 18.03))
            s12 = Line(s11 @ 1,(4.57, 3.81))
            s13 = Bezier(s12 @ 1,(5.33, 2.54),(6.60, 1.27),(8.13, 0.25))
            s14 = Bezier(s13 @ 1,(9.65, 1.52),(10.67, 2.79),(12.19, 4.57))
            s15 = Line(s14 @ 1,(14.99, 13.72))
            s16 = Line(s15 @ 1,(39.88, 14.22))
            s17 = Line(s16 @ 1,(39.88, 6.10))
            s18 = Line(s17 @ 1,(48.77, 6.10))
            s19 = Line(s18 @ 1,(49.02, 13.97))
            s20 = Line(s19 @ 1,(59.94, 13.72))
            s21 = Bezier(s20 @ 1,(65.28, 10.92),(70.87, 10.92),(76.96, 13.72))
            s22 = Bezier(s21 @ 1,(82.80, 12.70),(84.33, 13.72),(83.57, 20.57))
            s23 = Line(s22 @ 1, s0 @ 0)
        make_face()
    extrude(amount=5)

cutout.part.export_stl("cutout.stl")

#calipers_bin = gf.Bin(gf.BaseEqual(2, 6), height_in_units=4)
#bd.export_stl(calipers_bin, "calipers_bin.stl")


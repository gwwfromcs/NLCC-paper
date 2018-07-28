set terminal pngcairo color enhanced font "Arial,24" size 1000,1000
set output "200ry-compare.png"

set yr [-2:8]
plot '200Ry/p_band.dat' u 1:2 w l,\
     '200Ry-new_core_ps/p_band.dat' u 1:2 w l,\
     '200Ry-no-nlcc/p_band.dat' u 1:2 w l

set terminal pngcairo color enhanced font "Arial,24" size 1000,1000
set output "100ry-compare.png"

set yr [-2:8]
plot '100Ry/p_band.dat' u 1:2 w l,\
     '100Ry-new_core_ps/p_band.dat' u 1:2 w l,\
     '100Ry-no-nlcc/p_band.dat' u 1:2 w l

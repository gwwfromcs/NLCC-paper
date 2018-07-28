
set terminal pngcairo color enhanced font "Arial,24" size 1000,1000
set output "140ry-compare.png"

set yr [-2:8]
plot '140Ry/p_band.dat' u 1:2 w l,\
     '140Ry-new_core_ps/p_band.dat' u 1:2 w l,\
     '140Ry-no-nlcc/p_band.dat' u 1:2 w l

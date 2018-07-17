set xr [0:6]
plot 'ld1ps.wfc' u 1:2 w l t '', 'ld1ps.wfc' u 1:7 w l t '4p',\
     'ld1ps.wfc' u 1:5 w l t '', 'ld1ps.wfc' u 1:10 w l t '3d',\
     'ld1ps.wfc' u 1:6 w l t '', 'ld1ps.wfc' u 1:11 w l t '4s'

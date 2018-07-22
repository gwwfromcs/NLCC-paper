set terminal postscript eps color enhanced  font "Arial, 24" size 5,4
set output "compare_vxc_rhoc.eps"

#plot  '20ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/144.0):($2) w l t '20ryd',\
#      '40ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/216.0):($2) w l t '40ryd',\
#      '80ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/288.0):($2) w l t '80ryd',\
#      '120ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/360.0):($2) w l t '120ryd',\
#      '160ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/405.0):($2) w l t '160ryd',\
#      '250ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/512.0):($2) w l t '250ryd',\
#      'xy_vxcpot_average_test.dat' u (($1-1.0)/301.0):($2) w l t 'exact'

set multiplot 


set origin 0.03, 0.52
set size 0.97, 0.48
set logscale y
set xr [0:49.73]
set yr [1e-11:0.5]
set ylabel 'rho_core (Bohr^-3)'
set xtics ("" 10, "" 20, "" 30, "" 40 )
set key at 41.5,1e-8  samplen 1
plot '120ryd/xy_rhoc_average.dat' u (($1-1.0)/360.0*49.73):($2) w l t '480 Ryd',\
     '250ryd/xy_rhoc_average.dat' u (($1-1.0)/512.0*49.73):($2) w l t '1000 Ryd',\
     'xy_rhocexact_average.dat' u (($1-1.0)/405.0*49.73):($2) w l t 'exact'

set origin 0.06, 0.05
set size 0.92, 0.50
set arrow from 13.5,-3 to 19.5, -0.2 nohead lc rgb '#7f8287'
set arrow from 29.8,-3 to 30.0, -0.2 nohead lc rgb '#7f8287'
unset logscale y
set yr [-15.0:0.0]
set xtics 10
set xlabel 'z (Bohr)'
set ylabel 'V_{xc} (eV)'
set key at 43.5,-11 samplen 1
plot  '120ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/360.0*49.73):($2*13.605) w l t '480 Ryd',\
      '250ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/512.0*49.73):($2*13.605) w l t '1000 Ryd',\
      'xy_vxcpot_average_test.dat' u (($1-1.0)/301.0*49.73):($2*13.605) w l t 'exact'

unset arrow
set origin 0.32, 0.16
set size 0.35, 0.30
set yr [-1.2:0.0]
set xr [20.0:30.0]
set xtics 10 offset -0.5
set ytics 1  offset 0.5
unset xlabel
unset ylabel
plot  '120ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/360.0*49.73):($2*13.605) w l t '',\
      '250ryd/xy_vxcpot_average_test.dat' u (($1-1.0)/512.0*49.73):($2*13.605) w l t '',\
      'xy_vxcpot_average_test.dat' u (($1-1.0)/301.0*49.73):($2*13.605) w l lw 2 t ''

unset multiplot 

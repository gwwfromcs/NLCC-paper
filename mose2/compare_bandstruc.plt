#set terminal
set key at 14.6, -0.3
#set xrange [0:14.77083]
set xrange [6.805:6.905]
#set yrange [-4.0 : 8.5]
set yrange [2.0 : 8.5]
set arrow from  6.85517, -4.0 to  6.85517,  6.5 nohead
set xtics (" M "  0.00000," {/Symbol G} "  6.85517," K " 14.77083)
set ylabel 'E (eV)'

plot '120ryd/mose2_band.dat' u ($1):($2+1.0646) w p pt 1 t "core charges calculated with FFT", \
     '120ryd-no-nlcc/mose2_band.dat' u ($1):($2+1.0646) w p pt 2 t "no core correction"

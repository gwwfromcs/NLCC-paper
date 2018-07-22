nx=46
ny=46
awk -v nx="$nx" -v ny="$ny" 'BEGIN{average=0.0;nxy = 0; nz=0; minv=900; maxv=-900}
   {
   a[1]=$1; a[2]=$2; a[3]=$3; a[4]=$4; a[5]=$5; a[6]=$6;
   for(i=1; i<=6; i++)
   {
      if(nxy == nx*ny)
      {
          nz = nz+1;
          print nz,average/(nx-1)/(ny-1);
          average = a[i];
          nxy = 1;
          ix = 1
          iy = 1
          # printf "%6d %6d %6d %9.5f\n", ix, iy, nz+1, a[i]
      }
      else
      {
          if(a[i]!="") {
            ix = nxy/ny+1
            iy = nxy%ny+1
            # printf "%6d %6d %6d %9.5f\n", ix, iy, nz+1, a[i]
            nxy = nxy + 1;
            if(ix < nx && iy < ny) {
              average = average + a[i];
            }
          }
      }
      if(a[i]!="") {
        if(a[i]<minv) {minv = a[i]; };
        if(a[i]>maxv) {maxv = a[i]; };
      }
   }
   }END{printf "# %9.5f %9.5f\n",minv, maxv}' mose2_plot_vxc.xsf  > xy_vxcpot_average_test.dat

awk -v nx="$nx" -v ny="$ny" 'BEGIN{i=0;sum=0}{sum=sum+$2;if(NR%((nx-1)*(ny-1)) == 0 ) {i=i+1;print i,sum/(nx-1)/(ny-1); sum=0;} }' rhoc.dat > xy_rhoc_average.dat

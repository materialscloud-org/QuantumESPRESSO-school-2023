  EN=`grep "total energy =" ../init/dft.cpo     | awk '{print $4}'`
ENm1=`grep "total energy =" dft_n-1.cpo | awk '{print $4}'`
DE=`echo $ENm1 $EN | awk '{printf "%20.12f \n", ($1-$2)*13.6057*2}'`
#echo $EN $ENm1 $DE
e1=`grep -A 2 HOMO ki.cpo | tail -1`
e0=`grep -A 2 HOMO ../init/dft.cpo | tail -1`
#echo $e1 $e0
alpha=`echo $DE $e1 $e0 | awk '{printf "%12.4f \n", ($1+$3)/(-$2+$3)}'`
echo "     optimal alpha = "  $alpha

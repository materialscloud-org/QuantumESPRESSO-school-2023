printf "PROJWFC   ..."
projwfc.x -in Si.projwfc.in > Si.projwfc.out
echo " done"

printf "PLOTBAND ..."
# name files as expected by plotband.x
if [ ! -e si_bands_pbe.proj ]; then ln -s si_bands_pbe.projwfc_up si_bands_pbe.proj ; fi
plotband.x < plotband.in > plotband.out
echo " done"


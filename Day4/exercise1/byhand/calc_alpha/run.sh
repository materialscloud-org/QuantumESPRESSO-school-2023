echo "     DFT N-1 ..."
kcp.x -in dft_n-1.cpi > dft_n-1.cpo
echo "     KI unscreened ..."
kcp.x -in ki.cpi > ki.cpo
sh get_alpha.sh


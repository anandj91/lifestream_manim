set term pdf font 'Verdana,20'
unset key
unset border
unset xtic
unset ytic
set output "timeseries.pdf"
set datafile separator ","
set xlabel "Time"
set ylabel "Value"
set yrange [0:250]

set arrow from graph 0,0 to graph 0,1
set arrow from graph 0,0 to graph 1,0

plot "abp2.csv" u 1:2 w l lw 1 lc 2, \
     "abp2.csv" u 1:2 w p ls 7 pt 7 ps 0.15

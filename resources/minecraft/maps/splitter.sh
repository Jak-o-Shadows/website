tx=14320
ty=23424
xgap=512
ygap=512
xiter=$(($tx / $xgap))
yiter=$(($ty / $ygap))

for ((i=0; i<=$xiter; i++))
do
    for((j=o; j<=$yiter; j++))
    do
    x=$(($i*$xgap))
    y=$(($j*$ygap))
    convert test.png -crop ($xgap)x($ygap)+$x+$y +repage $i$j.png
    done
done


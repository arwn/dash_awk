
{
    if (NR > 0){
    if ($3 < 1.00) {
        print($0);
        total += $3
        count += 1
    }}
}

END{print total / count}

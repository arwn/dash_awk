{
    if (NR > 0 && $3 < 1.00){
        print $0
        total += $3
        count += 1
    }
}

END{printf "%.2f\n", total / count}

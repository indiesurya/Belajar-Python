for i in range(1,20) :
    habis = 0
    for j in range(1,i+1) :
        sisa = i%j
        if (sisa == 0) :
            habis += 1

    if(habis==2) :
        print(i,"adalah bilangan prima")
    else :
        print(i, "bukanlah bilangan prima")
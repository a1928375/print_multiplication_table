def print_multiplication_table(n):
    i=1
    j=1
    while i<=n:
        
        while True:
            if j<=n:
                h=i*j
                print (str(i)+"*"+str(j)+"="+str(h))
                j=j+1
            else:
                i=i+1
                j=1
                break
        if i>n:
            break
        if j<n:
            h=i*j
            print (str(i)+"*"+str(j)+"="+str(h))
            j=j+1
        else:
            i=i+1
            j=1
            break

print (print_multiplication_table(3))

def find_longest(k,ar):
    length=0
    for start in range(len(ar)):
        for end in range(start+1,len(ar)):
            print(ar[start:end], start, end)
            if len(set(ar[start:end]))<=k:
                if len(ar[start:end])>=length:
                    length=len(ar[start:end])
            else:
                break
    print length

ar=["z","a","c","d","c","a","e","e","d","f","g"]
k=3
find_longest(k, ar)
if __name__ == '__main__':
    ifstream = open('input.txt','r')
    S = ifstream.readline().replace('\n','')
    J = ifstream.readline().replace('\n','')
    ifstream.close()
    symbols = set(S)
    counts = {s: 0 for s in symbols}
    # count each s in J
    for j in J:
        if j in symbols:
            counts[j] += 1
    # sum calues of counts map
    sum = 0
    for v in counts.values():
        sum += v
    ofstream = open('output.txt', 'w')

    ofstream.write(str(sum))
    # if len(S) == 0 or len(J)==0:
    #     ofstream.write("0")
    # else:
    ofstream.close()

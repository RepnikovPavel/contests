if __name__ == '__main__':
    i_file = open('input.txt','r')
    a, b = [int(el) for el in i_file.readline().split(sep=" ")]
    i_file.close()
    out = str(a+b)
    o_file = open('output.txt','w')
    o_file.write(out)
    o_file.close()

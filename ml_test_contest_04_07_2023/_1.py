import sys
if __name__ == '__main__':
    input = sys.stdin
    output = sys.stdout
    while True:
        i_str = input.readline()
        if len(i_str) == 0:
            break
        a_s, b_s = i_str.split(sep=" ")
        a = int(a_s)
        b = int(b_s)
        o_str = str(a+b)
        output.write(o_str)

def with_index(seq):
    for i in xrange(len(seq)):
        yield i, seq[i]

def replace_all(seq, obj, replacement):
    for i, elem in with_index(seq):
        if elem == obj:
            seq[i] = replacement

def main():
    li = ['1', '3', '7', 'J']

    replace_all(li, 'J', '11')
    print li

if __name__ == "__main__":
    main()

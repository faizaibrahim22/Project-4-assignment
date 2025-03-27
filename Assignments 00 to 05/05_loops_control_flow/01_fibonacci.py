MAX_TERM_VALUE = 10000

def main():
    a,b = 0,1
    while a <= MAX_TERM_VALUE:
        print(a)
        a, b = b, a + b 

if __name__ == '__main__':
    main()

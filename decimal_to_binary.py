def decimal_to_binary(n):
    b = ''
    while(n>=1):
        x = n%2
        n = n//2
        b = str(x) + b

    print(b)

def main():
    n = int(input('Enter dicimal number : '))
    decimal_to_binary(n)

if __name__ == '__main__':
    main()
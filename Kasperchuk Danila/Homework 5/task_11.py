def main():
    a = float(input())
    b = float(input())
    c = float(input())

    D = b**2 - 4 * a * c
    if D < 0:
        print("No solutions")
    if a == 0:
        if b == 0:
            if c == 0:
                print("Infinite solutions")
            else:
                print("No solutions")
        else:
            x = -c / b
            print(round(x,2))    
    if D == 0:
        return (round((-b + D**0.5)/2*a, 2)) 
    elif D > 0:
        return ((round((-b + D**0.5)/(2*a), 2)), (round((-b - D**0.5)/(2*a), 2)))
if __name__ == '__main__':
    print(main())
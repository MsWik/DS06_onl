def main():
    n = int(input())
    m = int(input())
    n_set = set()
    m_set = set()

    total_set = set()

    for i in range(n):
        str = input()
        n_set.add(str)
    for j in range(m):
        str = input()
        m_set.add(str)

    total_set = n_set.union(m_set) - n_set.intersection(m_set)
    return len(total_set)
    
if __name__ == '__main__':
    print(main())
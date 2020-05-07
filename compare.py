

def compareTo(s1, s2):
    n = 0
    if len(s1) == 0 or len(s2) == 0:
        if len(s1) == 0 and len(s2) == 0:
            return 0
        elif len(s1) != 0 and len(s2) == 0:
            return 1
        elif len(s1) == 0 and len(s2) != 0:
            return -1

    if s1[n] < s2[n]:
        return -1

    elif s1[n] == s2[n]:
        return compareTo(s1[n + 1:], s2[n + 1:])

    elif s1[n] > s2[n]:
        return 1
    else:
        return 0


def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    print(compareTo(s1, s2))


if __name__ == "__main__":
    main()
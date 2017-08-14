#!/usr/bin/env python3

def main():
    items = []
    for a in range (2,101):
        for b in range (2,101):
            items.append(a**b)
    print(len(set(items)))


if __name__ == '__main__':
    main()

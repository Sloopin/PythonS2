def triangle(nr_stars):
    for i in range(1,nr_stars):
        print(" " * (nr_stars - i) + "*" * i)
    print("*" * nr_stars)

if __name__ == '__main__':
    triangle(10)

class Calculator:

    def sum(self, nr_a = "", nr_b = "", nr_c = ""):
        if nr_a != "" and nr_b != "":
            if nr_c == "":
                return nr_a + nr_b
            else:
                return nr_a + nr_b + nr_c
        else:
            print("Error: No numbers have been inserted!")
            return 0

    def sub(self, nr_a = "", nr_b = "", nr_c = ""):
        if nr_a != "" and nr_b != "":
            if nr_c == "":
                return nr_a - nr_b
            else:
                return nr_a - nr_b - nr_c
        else:
            print("Error: No numbers have been inserted!")
            return 0

    def multi(self, nr_a = "", nr_b = "", nr_c = ""):
        if nr_a != "" and nr_b != "":
            if nr_c == "":
                return nr_a * nr_b
            else:
                return nr_a * nr_b * nr_c
        else:
            print("Error: No numbers have been inserted!")
            return 0

    def divide(self, nr_a = "", nr_b = "", nr_c = ""):
        if nr_a != "" and nr_b != "":
            if nr_c == "":
                return nr_a / nr_b
            else:
                return (nr_a / nr_b) / nr_c
        else:
            print("Error: No numbers have been inserted!")
            return 0

    def linearEquation(self, a, b, c):
        return (c - d) / a
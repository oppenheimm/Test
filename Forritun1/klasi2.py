class Distribution:
    def __init__(self, file_stream=None):
        self.__distribution = {}
        if file_stream:
            self.__read_data(file_stream)

    def __str__(self):
        result_str = ""
        for num, count in sorted(self.__distribution.items()):
            result_str += "{}: {}\n".format(num, count)
        return result_str

    def __add__(self, other):
        """Adds two distributions. Returns a new distribution which contains the added
        frequencies of the two distributions"""
        result = Distribution()
        new_dist = self.__distribution.copy()
        for num, count in other.__distribution.items():
            if num in new_dist:
                new_dist[num] += count
            else:
                new_dist[num] = count
        result.set_distribution(new_dist)
        return result

    def __ge__(self, other):
        return self.average() >= other.average()

    def __read_data(self, file_object):
        """Reads each line from the file stream and updates the dictionary
        with counts of the numbers found in the stream"""
        for line in file_object:
            num_list = line.strip().split()
            for num in num_list:
                num = int(num)
                if num in self.__distribution:
                    self.__distribution[num] += 1
                else:
                    self.__distribution[num] = 1

    def set_distribution(self, distribution):
        self.__distribution = distribution

    def average(self):
        """Computes and returns the average for the distribution"""
        weighted_total = 0
        count_total = 0
        for num, count in self.__distribution.items():
            weighted_total += num * count
            count_total += count
        try:
            return weighted_total / count_total
        except ZeroDivisionError:
            return 0


dist1 = Distribution()
dist1.set_distribution({1: 5, 2: 3, 3: 7, 4: 4, 5: 6, 6: 4})
print("Dist1: ")
print(dist1)
print(dist1.average())


def open_file(filename):
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


filename = r"klasi2.txt"
file_stream = open_file(filename)

dist2 = Distribution(file_stream)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())

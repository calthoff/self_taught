
# http://tinyurl.com/hhdpkqh


class Data:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]


    def change_data(self, index, n):
        self.numbers[index] = n


data_one = Data()
data_one.numbers[0] = 100
print(data_one.numbers)


data_two = Data()
data_two.change_data(0, 100)
print(data_two.numbers)

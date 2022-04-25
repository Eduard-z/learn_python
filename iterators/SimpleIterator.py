class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    s_iter1 = SimpleIterator(3)
    # print(next(s_iter1))
    # print(next(s_iter1))
    # print(next(s_iter1))
    print(next(s_iter1))
    print(2 in s_iter1)
    print(list(s_iter1))

    # for i in s_iter1:
    #     print(i)

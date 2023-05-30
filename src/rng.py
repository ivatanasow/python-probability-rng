import random


class RandomGen(object):
    _random_nums = []
    _probabilities = []

    def __init__(self, random_nums, probabilities):
        self._random_nums = random_nums
        self._probabilities = probabilities

    def next_num(self):
        random_number = random.random()
        sum = 0
        for idx, prob in enumerate(self._probabilities):
            sum += prob
            if (random_number <= sum):
                return self._random_nums[idx]

        raise Exception("Cannot determine number")

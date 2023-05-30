import unittest

from rng import RandomGen


class TestRandomGen(unittest.TestCase):
    def test_next_num(self):
        rng = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        runs = 2000000
        hits = dict()

        for i in range(runs):
            number = rng.next_num()
            if number in hits:
                hits[number] = hits[number] + 1
            else:
                hits[number] = 1

        print("Hits:")
        print(hits)

        probabilities = dict()
        for key in hits:
            prob = hits[key] / runs
            probabilities[key] = round(prob, 2)

        print("Actual probability:")
        print(probabilities)


if __name__ == '__main__':
    unittest.main()

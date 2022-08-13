#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **balls) -> None:
        self.contents = []

        for key in balls.keys():
            for value in range(0, balls.get(key)):
                self.contents.append(str(key))


    def draw(self, amount):
        contents_len = len(self.contents)

        if amount >= contents_len:
            return self.contents

        pulled_balls = []

        for num in range(0, amount):
            random_number = random.randint(0, contents_len - 1)
            pulled_balls.append(self.contents[random_number])
            self.contents.remove(self.contents[random_number])

        return pulled_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_times = 0
    performed_experiments = 0
    experiments = num_experiments

    for experiment in range(experiments):
        hat_copy = copy.deepcopy(hat)
        taken_balls = hat_copy.draw(num_balls_drawn)
        extraced = Counter(taken_balls)
        contains_all = True

        for key, value in expected_balls.items():
            if key not in extraced.keys() or extraced.get(k) < expected_balls.get(k):
                contains_all = False
                break

    if contains_all == True:
        expected_times += 1

    performed_experiments += 1

    probability = expected_times / performed_experiments
    return probability


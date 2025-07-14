import copy
import random
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            setattr(self, color, count)
            self.contents += [color] * count
        self.placeholder_contents = copy.deepcopy(self.contents)

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            placeholder_deleted_balls = copy.deepcopy(self.contents)
            self.contents = []
            return placeholder_deleted_balls
        else:
            deleted_balls = random.sample(self.contents, num_balls)
            for ball in deleted_balls:
                self.contents.remove(ball)
            return deleted_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        hat.contents = copy.deepcopy(hat.placeholder_contents)
        valid = True
        drawn_balls = hat.draw(num_balls_drawn)
        for color,count in expected_balls.items():
            if drawn_balls.count(color) < count:
                valid = False
                break
        if valid:   
            success += 1
    probability = success / num_experiments
    return probability

test_hat = Hat(red=5, blue=3, green=2)
print(test_hat.contents)
test_hat.draw(3)
print(test_hat.contents)

hat = Hat(black=6, red=4, green=3)
print(experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000))

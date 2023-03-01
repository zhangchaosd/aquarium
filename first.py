import random
import time

from environment_config import *

class environment():  # eden
    def __init__(self, dimention) -> None:
        self._dimension = dimention
        pass

    def move(self, location, offset):
        assert len(offset) == self._dimension
        assert type(offset[0]) == int
        assert len(location) == self._dimension
        assert type(location[0]) == int
        pass
        new_location = tuple(sum(t) for t in zip(location, offset))
        food = new_location[0] // 2
        return new_location, food
    
    def change(self):
        # for manual control. etc add food
        pass

class life():  # adam
    def __init__(self, env) -> None:
        self.env = env
        self.location = [0]
        self.brain = 0  # resnet
        pass

    def make_decision(self):
        offset = [random.randint(-1,1)]
        self.location, new_food = self.env.move(self.location, offset)
        print(f'Now in {self.location}, Food: {new_food}')
        # train one step

# in: (location?) offset food smell


def main():
    eden = environment(DIMENTION)
    adam = life(eden)
    while True:
        adam.make_decision()
        time.sleep(1)


if __name__ == '__main__':
    main()
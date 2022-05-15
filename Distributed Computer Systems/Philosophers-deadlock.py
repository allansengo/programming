from threading import Thread, BoundedSemaphore
from time import sleep
from random import random


class Philosopher(Thread):
    def __init__(self, number, forks):
        self.number = number
        self.forks = forks
        self.left = number
        self.right = (number + 1) % len(forks)
        super().__init__()

    def think(self):
        print(f"Philosopher {self.number} starts thinking...")
        print(f"Philosopher {self.number} has become hungry!")

    def eat(self):
        print(f"Philosopher {self.number} starts eating!")
        sleep(random())
        print(f"Philosopher {self.number} has finished the consumption.")

    def run(self):
        for _ in range(10):
        #while True:
            self.think()
            with self.forks[self.left]:
                with self.forks[self.right]:
                    self.eat()



def main():
    num_philosophers = 5
    forks = [BoundedSemaphore(1) for _ in range(num_philosophers)]
    philosophers = [Philosopher(i, forks) for i in range(num_philosophers)]
    for phil in philosophers: phil.start()
    for phil in philosophers: phil.join()


if __name__ == "__main__":
    main()


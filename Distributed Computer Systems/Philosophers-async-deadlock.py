from asyncio import run, wait, Semaphore, sleep
from random import random


class Philosopher():
    def __init__(self, number, forks):
        self.number = number
        self.forks = forks
        self.left = number
        self.right = (number + 1) % len(forks)

    async def think(self):
        print(f"Philosopher {self.number} starts thinking...")
        print(f"Philosopher {self.number} has become hungry!")

    async def eat(self):
        print(f"Philosopher {self.number} starts eating!")
        await sleep(10*random())
        print(f"Philosopher {self.number} has finished the consumption.")

    async def dine(self):
        #for _ in range(10):
        while True:
            await self.think()
            async with self.forks[self.left]:
                async with self.forks[self.right]:
                    await self.eat()



async def run_philosophers():
    num_philosophers = 5
    forks = [Semaphore(1) for _ in range(num_philosophers)]
    philosophers = [Philosopher(i, forks) for i in range(num_philosophers)]
    await wait([philo.dine() for philo in philosophers])


def main():
    run(run_philosophers())


if __name__ == "__main__":
    main()


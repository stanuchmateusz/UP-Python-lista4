from time import sleep, time
from random import sample


class Ball:

    def __init__(self, number: int, extra_weigth: bool):
        self.number = number
        self.extra_weigth = extra_weigth

    def __str__(self):
        return f'{self.number} {self.extra_weigth}'


class LotteryMachine:
    def __init__(self):
        self.balls = []
        for i in range(1, 50):
            self.balls.append(Ball(i, False))

        for i in sample(range(49), 6):
            self.balls[i].extra_weigth = True

        self.__is_running = False

    def start(self):
        if not self.__is_running:
            print("Lottery Machine is starting")
            self.__is_running = True

        self.__shufflethelist()

    def stop(self):
        if self.__is_running:
            print("Lottery Machine is stopping")
            self.__is_running = False
        else:
            print("Lottery Machine is already stopped")

    def __shufflethelist(self):
        if self.__is_running:
            # zwraca liste 2 elementow do zamiany
            to_swap = sample(range(49), 2)
            sleep(0.01)
            # zamienia 2 elementy wylosowane wczesniej
            temp = self.balls[to_swap[0]]
            self.balls[to_swap[0]] = self.balls[to_swap[1]]
            self.balls[to_swap[1]] = temp
            # przeniesienie o jeden do przudu w liśnie kule które są wyważone
            for i in range(49):
                if self.balls[i].extra_weigth and i != 0:
                    temp = self.balls[i]
                    self.balls[i] = self.balls[i - 1]
                    self.balls[i - 1] = temp

    def __str__(self):
        return "".join(map(str, self.balls))


class LotteryPresenter:
    def main(self):
        print("Ladies and Gentlemen, welcome to the lottery machine")
        time_of_shuffle = int(input(
            "How long do you want to shuffle the balls? (in seconds) "))
        now = int(time())

        machine = LotteryMachine()
        while now+time_of_shuffle > int(time()):
            machine.start()
        machine.stop()
        for b in machine.balls:
            print(b.number, b.extra_weigth)


if __name__ == "__main__":
    LotteryPresenter().main()

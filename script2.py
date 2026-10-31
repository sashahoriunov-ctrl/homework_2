import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 70
        self.energy = 80
        self.progress = 50
        self.money = 1000
        self.random_money = 67
        self.alive = True
    def study(self):
        print("Я іду вчитися до IT Step Academy")
        self.progress += random.randint(1, 3)
        self.gladness += random.randint(-3, 2)
        self.energy -= random.randint(2, 5)
        self.money -= random.randint(30, 70)
    def mom_gives_money(self):
        self.random_money = random.randint(10, 100)
        print(f"Мама дала мені {self.random_money} грн!")
        self.money += self.random_money
        self.gladness += random.randint(1, 10)
    def chill(self):
        print ("Іду гуляти с друзями до двору")
        self.progress -= random.randint(0, 2)
        self.gladness += random.randint(2, 5)
        self.energy -= random.randint(1, 4)
        self.money -= random.randint(5, 20)
    def sleep(self):
        print ("Я лягаю спати")
        self.progress -= random.randint(0, 1)
        self.gladness += random.randint(1, 3)
        self.energy += random.randint(5, 10)
    def eat(self):
        print ("Орео - дуже смачні!")
        self.progress -= random.randint(0, 1)
        self.gladness += random.randint(1, 3)
        self.energy += random.randint(2, 6)
        self.money -= random.randint(5, 15)
    def info(self):
        print(f"Навчанність | {self.progress}")
        print(f"Радість     | {self.gladness}")
        print(f"Енергія     | {self.energy}")
        print(f"Гроші       | {self.money} грн")
    def is_alive(self):
        if self.progress <=0:
            print("В моєму мозку одне сміття! Нема прогресу!")
            self.alive = False
        if self.energy <=0:
            print("Моє тіло не має сил тримати самого себе")
            self.alive = False
        if self.gladness <=0:
            print("Я впав у дипресію")
            self.alive = False
        if self.money <=0:
            print ("В мене зовсім нема грошей...")
            self.alive = False
        if self.energy > 200:
            print ("Ура, я прошарений!")
            self.alive = False



    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)


        #============== v 1.0 ===========#
        func = [self.sleep, self.eat, self.study, self.chill, self.mom_gives_money]
        random.choice(func)()
        random.choice(func)()
        #================================#

        self.info()
        self.is_alive()
        print()

student = Student("Vasya")
for day in range(1, 366):
    if student.alive:
        student.live(day)





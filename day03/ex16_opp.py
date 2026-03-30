## ex16_opp.py 객체지향 클래스

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name}이(가) 짖습니다. 멍멍!')



poppy = Dog('뽀삐')
poppy.bark()

choco = Dog('초코')
choco.bark()
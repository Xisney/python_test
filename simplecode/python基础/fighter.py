"""

version: 0.1
author: Jason
date: 2019-06-01
"""
from random import randint, randrange
from abc import ABCMeta, abstractmethod


class Fighter(metaclass=ABCMeta):
    """战斗者"""
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    """奥特曼"""
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀"""
        if self._mp > 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury > 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法群体攻击"""
        if self._mp > 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(15, 25)
                return True
        else:
            return False

    def resume(self):
        """回复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '---%s奥特曼---\n' % self._name + \
               '生命值 %d\n' % self._hp + \
               '魔法值 %d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '---%s小怪兽\n' % self._name + \
               '生命值 %d\n' % self._hp


def is_any_alive(monsters):
    """判断是否有活着的小怪兽"""
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(utralman, monsters):
    print(utralman)
    for monster in monsters:
        print(monster, end=' ')


def main():
    u = Ultraman('砍你发型不乱', 1000, 120)
    m1 = Monster('伞兵一号', 250)
    m2 = Monster('永和站神', 550)
    m3 = Monster('卢本伟', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print("=====第%02d回合=====" % fight_round)
        skill = randint(1, 10)
        m = select_alive(ms)
        if skill <= 6:
            print('%s普通攻击%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击' % u.name)
            else:
                print('%s使用魔法攻击失败！' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀虐了%s' % (u.name, m.name))
            else:
                print('%s普通攻击%s' % (u.name, m.name))
                print('%s的魔法值恢复了%d' % (u.name, u.resume()))
        if m.alive:
            print('%s攻击了%s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n=====战斗结束！=====\n')
    if u.alive:
        print('奥特曼胜利！')
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()

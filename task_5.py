class Warrior:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        self.defence = True
        self.alive = True

    def hit(self, enemy):
        if not enemy.defence:
            enemy.health -= self.damage
        else:
            enemy.defence = False
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def defen(self):
        self.defence = True

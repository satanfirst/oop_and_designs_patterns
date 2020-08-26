from abc import ABC, abstractmethod


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    def get_stats(self):
        return self.stats


class AbstractPositive(AbstractEffect):
    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive, AbstractNegative):
    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects() + ['Berserk']
        return self.positive_effects

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        self.stats = self.base.get_stats()
        updates_val = {("Strength", "Endurance", "Agility", "Luck"): 7,
                       ("Perception", "Charisma", "Intelligence"): -3,
                       ("HP",): 50
                       }
        self.stats.update({key: self.base.get_stats()[key] + v for keys,
                                                                   v in updates_val.items() for key in keys})
        return self.stats


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects() + ['Blessing']
        return self.positive_effects

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats.update({k: self.stats[k] + 2 for k in
                           ('Strength', 'Perception', 'Endurance',
                            'Charisma', 'Intelligence', 'Agility', 'Luck')})
        return self.stats


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects() + ['Weakness']
        return self.negative_effects

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 4
        self.stats['Endurance'] -= 4
        self.stats['Agility'] -= 4
        return self.stats


class Curse(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects() + ['Curse']
        return self.negative_effects

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats.update({k: self.stats[k] - 2 for k in
                           ('Strength', 'Perception', 'Endurance', 'Charisma',
                            'Intelligence', 'Agility', 'Luck')})
        return self.stats


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects() + ['EvilEye']
        return self.negative_effects

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Luck"] -= 10
        return self.stats

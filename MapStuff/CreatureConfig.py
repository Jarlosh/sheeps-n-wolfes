from enum import Enum


class CreatureConfig:
    def __init__(self, view, hp=0, max_hp=0, small_cut=0, hard_cut=0):
        self.hp = hp
        self.max_hp = max_hp
        self.small_cut = small_cut
        self.hard_cut = hard_cut
        self.view = view


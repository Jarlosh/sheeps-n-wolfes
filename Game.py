from MapStuff.GameLogic.StepCollector import StepCollector
from Step.step import Step


class Game:
    def __init__(self, game_map):
        self.finished = False
        self.game_map = game_map
        # self.step_collector = StepCollector()


    def resolve_to_end(self):
        while not self.is_game_finished():
            self.play_step()
        self.save()


    def save(self):
        pass

    def is_game_finished(self):
        # make some checks here
        return self.finished

    def play_step(self):
        step = Step()
        res = step.resolve()


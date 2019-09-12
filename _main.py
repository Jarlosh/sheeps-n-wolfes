from MapStuff.GameLogic.DecisionFunc import DecisionFunc
from MapStuff.GameLogic.Behaviour import Behaviour
from MapStuff.GameLogic.StepCollector import StepCollector
from MapStuff.GameLogic.ViewGetter import ViewGetter
from MapStuff.GameMap import GameMap
from MapStuff.Misc.DirectionEnum import Direction

cra = [5, 5, 0]
gm = GameMap.make_from_args(8, 8, cra)

vr = {
    Direction.North: 2, Direction.West: 2, Direction.East: 2, Direction.South: 0}
w = [1 for i in range(15)]
ls = [1]
df = DecisionFunc(15, ls, w)
vf = ViewGetter(vr)

sb = wb = Behaviour(df, vf)
col = StepCollector(gm, sb, wb)

gm.collect_step(col)
gm.collect_step(col)
s = gm.collect_step(col)
a = len(s[0])
b = len(s[1])
pass






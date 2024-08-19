from workPlace.base_vars import Locations


class DecideAndAct(Locations):
    def __init__(self, m3c, mq, mp, qb, pb):
        super().__init__()
        self.matches_triple_coords = m3c
        self.matches_quad_coords = mq
        self.matches_penta_coords = mp
        self.quad_bool = qb
        self.penta_bool = pb

    def worker(self):
        ...

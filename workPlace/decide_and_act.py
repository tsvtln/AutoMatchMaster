from workPlace.base_vars import Locations


class DecideAndAct(Locations):
    def __init__(self, m3c, mq, mp, qb, pb):
        super().__init__()
        self.matches_triple_coords = m3c
        self.matches_quad_coords = mq
        self.matches_penta_coords = mp
        self.quad_bool = qb
        self.penta_bool = pb
        self.worker()

    def worker(self):
        if self.penta_bool:
            pass
        elif self.quad_bool:
            pass
        else:
            pass
        # print(f'Triple coords: {self.matches_triple_coords}\n'
        #       f'Quad coords: {self.matches_quad_coords}\n'
        #       f'Penta coords: {self.matches_penta_coords}\n'
        #       f'Quad bool: {self.quad_bool}\n'
        #       f'Penta bool: {self.penta_bool}')


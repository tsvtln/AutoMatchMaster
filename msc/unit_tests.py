import unittest
from workPlace.m3x_walker import MatrixWalker
import msc.matrix_schemas as m3x_schemas


class TestMoves(unittest.TestCase):
    def setUp(self):
        self.m3x_right_happy = m3x_schemas.happy_matrix_triple()[0]
        self.m3x_left_happy = m3x_schemas.happy_matrix_triple()[1]
        self.m3x_down_happy = m3x_schemas.happy_matrix_triple()[2]
        self.m3x_up_happy = m3x_schemas.happy_matrix_triple()[3]

        self.m3x_right_ovb = m3x_schemas.overboard_matrix_triple()[0]
        self.m3x_left_ovb = m3x_schemas.overboard_matrix_triple()[1]
        self.m3x_down_ovb = m3x_schemas.overboard_matrix_triple()[2]
        self.m3x_up_ovb = m3x_schemas.overboard_matrix_triple()[3]

        self.m3x_right_quad_happy = m3x_schemas.happy_matrix_quad()[0]
        self.m3x_left_quad_happy = m3x_schemas.happy_matrix_quad()[1]
        self.m3x_down_quad_happy = m3x_schemas.happy_matrix_quad()[2]
        self.m3x_up_quad_happy = m3x_schemas.happy_matrix_quad()[3]

        self.m3x_right_quad_ovb = m3x_schemas.overboard_matrix_quad()[0]
        self.m3x_left_quad_ovb = m3x_schemas.overboard_matrix_quad()[1]
        self.m3x_down_quad_ovb = m3x_schemas.overboard_matrix_quad()[2]
        self.m3x_up_quad_ovb = m3x_schemas.overboard_matrix_quad()[3]

        self.m3x_right_penta = m3x_schemas.happy_matrix_penta()[0]
        self.m3x_left_penta = m3x_schemas.happy_matrix_penta()[1]
        self.m3x_down_penta = m3x_schemas.happy_matrix_penta()[2]
        self.m3x_up_penta = m3x_schemas.happy_matrix_penta()[3]


    def test_right_happy(self):
        m3x_walker = MatrixWalker(self.m3x_right_happy)
        value_verify = m3x_walker.matches_triple['match_right']['green']
        self.assertEqual(value_verify[0], (3, 2), 'Right Move Happy FAILED')
        # print('Right Move Happy PASSED')



if __name__ == '__main__':
    unittest.main()

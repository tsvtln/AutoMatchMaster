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
        self.assertEqual(value_verify[0], (3, 2), 'FAILED Happy Triple Right Move')
        print('PASSED Happy Triple Right Move')

    def test_left_happy(self):
        m3x_walker = MatrixWalker(self.m3x_left_happy)
        value_verify = m3x_walker.matches_triple['match_left']['green']
        self.assertEqual(value_verify[0], (1, 6), 'FAILED Happy Triple Left Move')
        print('PASSED Happy Triple Left Move')

    def test_down_happy(self):
        m3x_walker = MatrixWalker(self.m3x_down_happy)
        value_verify = m3x_walker.matches_triple['match_down']['blue']
        self.assertEqual(value_verify[0], (0, 3), 'FAILED Happy Triple  Down Move')
        self.assertEqual(value_verify[2], (1, 4), 'FAILED Happy Triple  Down Move')
        print('PASSED Happy Triple Down Move')

    def test_up_happy(self):
        m3x_walker = MatrixWalker(self.m3x_up_happy)
        value_verify = m3x_walker.matches_triple['match_up']['blue']
        self.assertEqual(value_verify[0], (6, 4), 'FAILED Happy Triple Up Move')
        print('PASSED Happy Triple Up Move')

    def test_overboard_triple_right(self):
        m3x_walker = MatrixWalker(self.m3x_right_ovb)
        value_verify = m3x_walker.matches_triple['match_right']['green']
        self.assertIsNot(value_verify[0], (1, 6), 'FAILED Overboard Triple Right')
        print('PASSED Overboard Triple Right')

    def test_overboard_triple_left(self):
        m3x_walker = MatrixWalker(self.m3x_left_ovb)
        value_verify = m3x_walker.matches_triple['match_left']['green']
        self.assertIsNot(value_verify[0], (2, 0), 'FAILED Overboard Triple Left')
        print('PASSED Overboard Triple Left')

    def test_overboard_triple_down(self):
        m3x_walker = MatrixWalker(self.m3x_down_ovb)
        value_verify = m3x_walker.matches_triple['match_down']['blue']
        self.assertIsNot(value_verify[0], (6, 4), 'FAILED Overboard Triple Down')
        print('PASSED Overboard Triple Down')

    def test_overboard_triple_up(self):
        m3x_walker = MatrixWalker(self.m3x_up_ovb)
        value_verify = m3x_walker.matches_triple['match_up']['red']
        with self.assertRaises(IndexError):
            self.assertIsNot(value_verify[0], (0, 4), 'FAILED Overboard Triple Up')
        print('PASSED Overboard Triple Up')

    def test_right_quad_happy(self):
        m3x_walker = MatrixWalker(self.m3x_right_quad_happy)
        value_verify = m3x_walker.matches_quad['match_right']['red']
        quad_verify = m3x_walker.quad
        self.assertEqual(value_verify[0], (1, 3), 'FAILED Quad Right Move')
        self.assertIs(quad_verify, True, 'FAILED Quad Right Move Bool')
        print('PASSED Happy Quad Right Move & Bool verification')

    def test_left_quad_happy(self):
        m3x_walker = MatrixWalker(self.m3x_left_quad_happy)
        value_verify = m3x_walker.matches_quad['match_left']['green']
        quad_verify = m3x_walker.quad
        self.assertEqual(value_verify[0], (3, 4), 'FAILED Quad Left Move')
        self.assertIs(quad_verify, True, 'FAILED Quad Left Move Bool')
        print('PASSED Happy Quad Left Move & Bool verification')

    def test_down_quad_happy(self):
        m3x_walker = MatrixWalker(self.m3x_down_quad_happy)
        value_verify = m3x_walker.matches_quad['match_down']['yellow']
        quad_verify = m3x_walker.quad
        self.assertEqual(value_verify[0], (4, 4), 'FAILED Quad Down Move')
        self.assertIs(quad_verify, True, 'FAILED Quad Down Move Bool')
        print('PASSED Happy Quad Down Move & Bool verification')

    def test_up_quad_happy(self):
        m3x_walker = MatrixWalker(self.m3x_up_quad_happy)
        value_verify = m3x_walker.matches_quad['match_up']['green']
        quad_verify = m3x_walker.quad
        self.assertEqual(value_verify[0], (2, 2), 'FAILED Quad Up Move')
        self.assertIs(quad_verify, True, 'FAILED Quad Up Move Bool')
        print('PASSED Happy Quad Up Move & Bool verification')

    def test_right_quad_overboard(self):
        m3x_walker = MatrixWalker(self.m3x_right_quad_ovb)
        value_verify = m3x_walker.matches_quad['match_right']['green']
        quad_verify = m3x_walker.quad
        with self.assertRaises(IndexError):
            self.assertIsNot(value_verify[0], (6, 1), 'FAILED Quad Overboard Right Move')
        self.assertIs(quad_verify, False, 'FAILED Quad Overboard Right Move Bool')
        print('PASSED Overboard Quad Right Move & Bool verification')

    def test_left_quad_overboard(self):
        m3x_walker = MatrixWalker(self.m3x_left_quad_ovb)
        value_verify = m3x_walker.matches_quad['match_left']['red']
        quad_verify = m3x_walker.quad
        with self.assertRaises(IndexError):
            self.assertIsNot(value_verify[0], (3, 0), 'FAILED Quad Overboard Left Move')
        self.assertIs(quad_verify, False, 'FAILED Quad Overboard Left Move Bool')
        print('PASSED Overboard Quad Left Move & Bool verification')

    def test_down_quad_overboard(self):
        m3x_walker = MatrixWalker(self.m3x_down_quad_ovb)
        value_verify = m3x_walker.matches_quad['match_down']['blue']
        quad_verify = m3x_walker.quad
        with self.assertRaises(IndexError):
            self.assertIsNot(value_verify[0], (6, 3), 'FAILED Quad Overboard Down Move')
        self.assertIs(quad_verify, False, 'FAILED Quad Overboard Down Move Bool')
        print('PASSED Overboard Quad Down Move & Bool verification')

    def test_up_quad_overboard(self):
        m3x_walker = MatrixWalker(self.m3x_up_quad_ovb)
        value_verify = m3x_walker.matches_quad['match_up']['green']
        quad_verify = m3x_walker.quad
        with self.assertRaises(IndexError):
            self.assertIsNot(value_verify[0], (0, 5), 'FAILED Quad Overboard Up Move')
        self.assertIs(quad_verify, False, 'FAILED Quad Overboard Up Move Bool')
        print('PASSED Overboard Quad Up Move & Bool Verification')

    def test_right_penta_happy(self):
        m3x_walker = MatrixWalker(self.m3x_right_penta)
        value_verify = m3x_walker.matches_penta['match_right']['blue']
        penta_verify = m3x_walker.penta
        self.assertEqual(value_verify[0], (4, 1), 'FAILED Penta Right Move')
        self.assertEqual(penta_verify, True, 'FAILED Penta Right Move Bool')
        print('PASSED Penta Right Move')

    '''
    Quad will also get a hit before this penta move, as the down check is found in any case.
    ToDo:
        Decide if to keep this check in the m3x_walker.py as it can be considered obsolete with
        the current behaviour (stopping all check when quad/penta is found) or to keep looking for penta, even if
        quad is found.
    '''
    # def test_left_penta_happy(self):
    #     m3x_walker = MatrixWalker(self.m3x_left_penta)
    #     value_verify = m3x_walker.matches_penta['match_left']['green']
    #     penta_verify = m3x_walker.penta
    #     self.assertEqual(value_verify[0], (3, 4), 'FAILED Penta Left Move')
    #     self.assertEqual(penta_verify, True, 'FAILED Penta Left Move Bool')
    #     print('PASSED Penta Left Move')

    def test_down_penta_happy(self):
        m3x_walker = MatrixWalker(self.m3x_down_penta)
        value_verify = m3x_walker.matches_penta['match_down']['green']
        penta_verify = m3x_walker.penta
        self.assertEqual(value_verify[0], (2, 3), 'FAILED Penta Down Move')
        self.assertEqual(penta_verify, True, 'FAILED Penta Down Move Bool')
        print('PASSED Penta Down Move')

    def test_up_penta_happy(self):
        m3x_walker = MatrixWalker(self.m3x_up_penta)
        value_verify = m3x_walker.matches_penta['match_up']['blue']
        penta_verify = m3x_walker.penta
        self.assertEqual(value_verify[0], (5, 2), 'FAILED Penta Up Move')
        self.assertEqual(penta_verify, True, 'FAILED Penta Up Move Bool')
        print('PASSED Penta Up Move')



if __name__ == '__main__':
    unittest.main()

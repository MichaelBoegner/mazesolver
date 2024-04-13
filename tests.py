import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )

    def test_maze_origin_point(self):
        num_cols = 12
        num_rows = 10
        x1 = 100
        y1 = 100
        m1 = Maze(x1,y1,num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.x1,
            x1
        )
        self.assertEqual(
            m1.y1,
            y1
        )

    def test_maze_create_10000_cells(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows
        )
        self.assertEqual(
            len(m1.cells) * len(m1.cells[0]),
            10000
        )

    def test_maze_create_entrance_exit(self):
        m1 = Maze(10, 10, 5, 5, 100, 100)
        self.assertFalse(
            m1.cells[0][0].has_top_wall
        )
        self.assertFalse(
            m1.cells[m1.num_cols-1][m1.num_rows-1].has_bottom_wall
        )

if __name__ == "__main__":
    unittest.main()

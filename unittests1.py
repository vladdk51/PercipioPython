"""Unit tests for "function lab.py" 

Run with:
    python unittests1.py
or:
    python -m unittest unittests1 -v
"""

import contextlib
import importlib.util
import io
import os
import unittest

SOURCE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "function lab.py")


def load_module():
    spec = importlib.util.spec_from_file_location("function_lab", SOURCE_FILE)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


functions_lab = load_module()


class TestFunctionLab(unittest.TestCase):
    def test_get_force(self):
        self.assertEqual(functions_lab.get_force(2, 3), 6)
        self.assertEqual(functions_lab.get_force(0, 10), 0)
        # the train from the lab: 22680 kg accelerating at 10 m/s^2
        self.assertEqual(functions_lab.get_force(22680, 10), 226800)
        self.assertEqual(functions_lab.train_force, 226800)

    def test_get_energy(self):
        # default speed of light: 1 kg -> 9 * 10**16 joules
        self.assertEqual(functions_lab.get_energy(1), 9 * 10**16)
        self.assertEqual(functions_lab.bomb_energy, 9 * 10**16)
        # custom value of c
        self.assertEqual(functions_lab.get_energy(2, 10), 200)
        self.assertEqual(functions_lab.get_energy(0), 0)

    def test_get_work(self):
        self.assertEqual(functions_lab.get_work(2, 3, 4), 24)
        self.assertEqual(functions_lab.get_work(22680, 10, 100), 22680000)
        self.assertEqual(functions_lab.train_work, 22680000)
        # no distance means no work
        self.assertEqual(functions_lab.get_work(22680, 10, 0), 0)

    def test_f_to_c(self):
        self.assertAlmostEqual(functions_lab.f_to_c(32), 0)
        self.assertAlmostEqual(functions_lab.f_to_c(212), 100)
        self.assertAlmostEqual(functions_lab.f_to_c(-40), -40)
        self.assertAlmostEqual(functions_lab.f_to_c(100), 37.77777777777778)
        self.assertAlmostEqual(functions_lab.f100_in_celsius, 37.77777777777778)

    def test_c_to_f(self):
        self.assertAlmostEqual(functions_lab.c_to_f(0), 32)
        self.assertAlmostEqual(functions_lab.c_to_f(100), 212)
        self.assertAlmostEqual(functions_lab.c_to_f(-40), -40)
        self.assertAlmostEqual(functions_lab.c0_in_fahrenheit, 32)
        # converting there and back should return the starting value
        self.assertAlmostEqual(functions_lab.f_to_c(functions_lab.c_to_f(25)), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)

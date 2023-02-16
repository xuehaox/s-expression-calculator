#!/usr/bin/env python3

import sys 
import unittest
from subprocess import check_output


def run_calc(expr: str) -> str:
    return check_output('python3 ./calc.py {}'.format(expr), shell=True).decode(sys.stdout.encoding).strip()

class TestLexer(unittest.TestCase):
    
    def test_calc(self):

        self.assertEqual(
            run_calc("0"), 
            str(0)
        )

        self.assertEqual(
            run_calc("13147483647"), 
            str(13147483647)
        )

        self.assertEqual(
            run_calc('"(add 1547483647 1547483647)"'), 
            str(1547483647 + 1547483647)
        )

        self.assertEqual(
            run_calc('"(add 1 1)"'), 
            str(2)
        )

        self.assertEqual(
            run_calc('"(add 123 456)"'), 
            str(579)
        )

        self.assertEqual(
            run_calc('"(add 0 (add 3 4))"'), 
            str(7)
        )

        self.assertEqual(
            run_calc('"(add 3 (add (add 3 3) 3))"'), 
            str(12)
        )

        self.assertEqual(
            run_calc('"(multiply 1 1)"'), 
            str(1)
        )

        self.assertEqual(
            run_calc('"(multiply 0 (multiply 3 4))"'), 
            str(0)
        )

        self.assertEqual(
            run_calc('"(multiply 3 (multiply (multiply 3 3) 3))"'), 
            str(81)
        )

        self.assertEqual(
            run_calc('"(add 1 (multiply 2 3))"'), 
            str(7)
        )

        self.assertEqual(
            run_calc('"(multiply 2 (add (multiply 2 3) 8))"'), 
            str(28)
        )

        self.assertEqual(
            run_calc('"(multiply (add 1 2) 3)"'), 
            str(9)
        )

        self.assertEqual(
            run_calc('"(multiply 2 (add (multiply (multiply 2 (add (multiply 2 (multiply 2 (add (multiply 2 3) 8))) 8)) 3) 8))"'), 
            str(784)
        )

        # test running time
        """
        self.assertEqual(
            run_calc('"(multiply (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply (multiply (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8))))))) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (add (multiply (multiply 2 (add (multiply 2 3) 8)) (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply (multiply (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8))))))) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8))))))) 8)) (add (multiply 2 3) 8)))))) (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply (multiply (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 (multiply 2 (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8))))))) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (multiply 3 (multiply 2 (add (multiply 2 3) (multiply (multiply 2 (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8)))))) (add (multiply (multiply 2 (add (multiply 2 3) 8)) 3) 8)) (add (multiply 2 3) 8))))))"'), 
            str(0)
        )
        """



if __name__ == '__main__':
    unittest.main()
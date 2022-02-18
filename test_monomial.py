import inspect
import unittest
# import doctest

from snake_egg import EGraph, Rewrite, Var, vars

from collections import namedtuple

Monomial = namedtuple('Monomial', 'l o r')
# SumPoly = namedtuple('SumPoly', ['n', 'subpolys'])
# ProdPoly = namedtuple('ProdPoly', ['n', 'subpolys'])

l, o, r = vars('l o r')
l1, o1, r1 = vars('l1 o1 r1')
l2, o2, r2 = vars('l2 o2 r2')

rules = [
    Rewrite(Monomial(l, o, r), Monomial(r, o, l)),
    Rewrite(Monomial(Monomial(l1, o1, r1), o, r), Monomial(r, o, Monomial(l1, o1, r1))),
    Rewrite(Monomial(Monomial(l1, o1, r1), o, Monomial(l2, o1, r2)), Monomial(Monomial(l2, o1, r2), o, Monomial(l1, o1, r1)))
]

class TestEGraph(unittest.TestCase):
    def test_simple(self):
        egraph = EGraph()
        eq1 = egraph.add(Monomial('x', '==', 'y'))
        noeq1 = egraph.add(Monomial('a', '!=', 'b'))
        noeq2 = egraph.add(Monomial('b', '!=', 'a'))


        egraph.run(rules, iter_limit=2)

        # self.assertTrue(egraph.union(2, Monomial('u', '==', 'v'), Monomial('v', '==', 'u')))

        # extract two separately
        self.assertNotEqual(egraph.extract(eq1), egraph.extract(noeq1))
        # extract two at same time
        a, b = egraph.extract(noeq1, noeq2)
        self.assertEqual(a, b)
        print("Success")


if __name__ == '__main__':
    # import snake_egg
    # print("--- doc tests ---")
    # failed, tested = doctest.testmod(snake_egg, verbose=True, report=True)
    # if failed > 0:
    #     exit(1)
    print("\n\n--- unit tests ---")
    unittest.main(verbosity=2)


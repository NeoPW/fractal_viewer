import unittest
from fractal_viewer.algorithms.lindemayer_system import Rule, Rules, LSystem

class TestLindemayerSytem(unittest.TestCase):

    def test_algae(self):
        r1 = Rule('A', 'AB')
        r2 = Rule('B', 'A')
        rules = Rules([r1, r2])
        start = 'A'
        system = LSystem(start, rules)

        assert system.last == 'A'
        assert system.applyAllReplacementRules() == 'AB'
        assert system.applyAllReplacementRules() == 'ABA'
        assert system.applyAllReplacementRules() == 'ABAAB'
        assert system.applyAllReplacementRules() == 'ABAABABA'
        assert system.applyAllReplacementRules() == 'ABAABABAABAAB'
        assert system.applyAllReplacementRules() == 'ABAABABAABAABABAABABA'
        assert system.applyAllReplacementRules() == 'ABAABABAABAABABAABABAABAABABAABAAB'

    def test_algea_step_by_step(self):
        r1 = Rule('A', 'AB')
        r2 = Rule('B', 'A')
        rules = Rules([r1, r2])
        start = 'A'
        system = LSystem(start, rules)

        assert system.last == 'A'
        assert system.applyRulesByOneStep() == 'AB'   
        assert system.applyRulesByOneStep() == 'AB'
        assert system.applyRulesByOneStep() == 'A'


    def test_binary_tree(self):
        r1 = Rule('1', '11')
        r2 = Rule('0', '1[0]0')
        start = '0'
        system = LSystem(start, Rules([r1, r2]))

        assert system.last == '0'
        assert system.applyAllReplacementRules() == '1[0]0'
        assert system.last == '1[0]0'
        assert system.applyAllReplacementRules() == '11[1[0]0]1[0]0'
        assert system.applyAllReplacementRules() == '1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0'

    def test_koch(self):
        r1 = Rule('F', 'F+F-F-F+F')
        start = 'F'
        system = LSystem(start, Rules([r1]))

        assert system.last == 'F'
        assert system.applyAllReplacementRules() == 'F+F-F-F+F'
        assert system.applyAllReplacementRules() == 'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F'
        assert system.applyAllReplacementRules() == 'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F'

    def test_koch_step_by_step(self):
        r1 = Rule('F', 'F+F-F-F+F')
        start = 'F'
        system = LSystem(start, Rules([r1]))

        assert system.last == 'F'
        assert system.applyRulesByOneStep() == 'F+F-F-F+F'
        assert system.applyRulesByOneStep() == 'F+F-F-F+F'
        assert system.applyRulesByOneStep() == '+'
        assert system.applyRulesByOneStep() == 'F+F-F-F+F'
        assert system.applyRulesByOneStep() == '-'

    def test_fractal_plant(self):
        r1 = Rule('X', 'F+[[X]-X]-F[-FX]+X')
        r2 = Rule('F', 'FF')
        start = '-X'
        system = LSystem(start, Rules([r1, r2]))

        assert system.last == '-X'
        assert system.applyAllReplacementRules() == '-F+[[X]-X]-F[-FX]+X'
        assert system.applyAllReplacementRules() == '-FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X'
        assert system.applyAllReplacementRules() == '-FFFF+[[FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X]-FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X]-FFFF[-FFFFFF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X]+FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X'
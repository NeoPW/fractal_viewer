

class Rule:
    def __init__(self, pre: str, succ: str):
        self.pre = pre
        self.succ = succ

class Rules:
    def __init__(self, rules: list[Rule]):
        self.rules: dict[str, str] = {}
        for rule in rules:
            self.rules[rule.pre] = rule.succ

    def replace(self, pre) -> str:
        return self.rules.get(pre, pre)

class LSystem:
    def __init__(self, start: str, rules: Rules):
        self.start = start
        self.rules = rules
        self.curr = ''
        self.n = 0

        self.step = 0
        self.last = start

    def applyAllReplacementRules(self) -> str:
        for char in self.last:
            self.curr += self.rules.replace(char)

        self.last = self.curr
        self.curr = ''
        self.n += 1
        print(self.last)
        return self.last
    
    def applyRulesByOneStep(self) -> str:
        temp = self.rules.replace(self.last[self.step])
        self.curr += temp
        self.step += 1

        if self.step == len(self.last):
            self.last = self.curr
            self.curr = ''
            self.step = 0
            return temp

        return temp

class LSystemDrawer:
    def __init__(self):
        self.pos = 0
        self.system: LSystem = self._initSystem()

    def _initSystem(self) -> LSystem:
        pass

    def step(self) -> list[str]:
        if self.pos == len(self.system.last):
            self.pos = 0
            self.system.applyAllReplacementRules()

        return self.ruleExecution(self.system.last[self.pos])

    def ruleExecution(self, rule: Rule) -> list[str]:
        pass
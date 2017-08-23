
from testing import ModuleTestBase, FunctionTestReturningFloat, StagedTest

class Homework4Test (ModuleTestBase):

    fun_name = "max_relative_frequency"
    expl_str = "the most frequent letters are {}, which occur {} times (each); the total number of letters is {}"

    s0_tests = (
        (('''sufficit''',), 0.25, expl_str, ['f', 'i'], 2, 8),
        (('''mississippi''',), 0.36363, expl_str, ['i', 's'], 4, 11)
    )

    s1_tests = (
        (('''nullius in verba''',), 0.14286, expl_str, ['i', 'l', 'n', 'u'], 2, 14),
        (('''quantum sufficit''',), 0.20000, expl_str, ['u'], 3, 15),
        (('''semper ad meliora''',), 0.20000, expl_str, ['e'], 3, 15),
        (('''si tacuisses philosophus mansisses''',), 0.32258, expl_str, ['s'], 10, 31),
        (('''quam bene non quantum''',), 0.22222, expl_str, ['n'], 4, 18),
        (('''pecunia si uti scis ancilla est si nescis domina''',), 0.20000, expl_str, ['i'], 8, 40)
    )

    s2_tests = (
        (('''Nullius In Verba''',), 0.14286, expl_str, ['i', 'l', 'n', 'u'], 2, 14),
        (('''qUaNtuM sUffiCit''',), 0.20000, expl_str, ['u'], 3, 15),
        (('''semper ad MELIORA''',), 0.20000, expl_str, ['e'], 3, 15),
        (('''si TACUISSES philoSOPHUS Mansisses''',), 0.32258, expl_str, ['s'], 10, 31),
        (('''quam BENE NON QUANTUM''',), 0.22222, expl_str, ['n'], 4, 18)
    )

    s3_tests = (
        (('''pecunia, si uti scis, ancilla est; si nescis, domina''',), 0.20000, expl_str, ['i'], 8, 40),
        (('''In fact, it is difficult to construct a solitary thought
without using that most common symbol. It is slow going at first, but
with caution and hours of training you can gradually gain facility.''',), 0.14013, expl_str, ['t'], 22, 157),
        (('''Preheat oven to 350 degrees F (175 degrees C). Grease a 9x9 inch baking pan.''',), 0.22000, expl_str, ['e'], 11, 50),
        (('''42 minutes and 42 seconds?''',), 0.17647, expl_str, ['n', 's'], 3, 17),
        (('''void splurf { i++;
  if ([i % 5] = 5) { splurf(); }''',), 0.20000, expl_str, ['i'], 4, 20),
        (('''53mper ad m3l10ra''',), 0.20000, expl_str, ['a', 'm', 'r'], 2, 10),
        (('''qu4m b3n3 n0n quan7um''',), 0.30769, expl_str, ['n'], 4, 13),
        (('''si tacui55es ph1los0phus m4nsi55es''',), 0.25000, expl_str, ['s'], 6, 24)
    )

    s4_tests = (
        (('''1437746094.5735958''',), 0.00000, expl_str, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 0, 0),
        (('''mea navis aëricumbens anguillis abundat''',), 0.17647, expl_str, ['a'], 6, 34)
        )

    def test_homework_4(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft0 = FunctionTestReturningFloat(fun, self.s0_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft1 = FunctionTestReturningFloat(fun, self.s1_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft2 = FunctionTestReturningFloat(fun, self.s2_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft3 = FunctionTestReturningFloat(fun, self.s3_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft4 = FunctionTestReturningFloat(fun, self.s4_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        st = StagedTest((ft0, ft1, ft2, ft3, ft4), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_4(False)
        print(msg)

    ## end Homework4Test


## To produce less verbose output, change verbose from 3 to 2 or 1:

Homework4Test("homework4.py", verbose = 3).run()

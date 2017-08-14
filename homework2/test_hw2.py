
import numpy

from testing import ModuleTestBase, FunctionTestWithExplanation, StagedTest

class Homework2Test (ModuleTestBase):

    fun_name = "triangular"
    expl_str = "the {}th triangular number is {} = {}"

    s1_tests = (
        ((1,), 1, expl_str, 1, " + ".join([str(i) for i in range(2)]), 1),
        ((2,), 3, expl_str, 2, " + ".join([str(i) for i in range(3)]), 3),
        ((3,), 6, expl_str, 3, " + ".join([str(i) for i in range(4)]), 6),
        ((4,), 10, expl_str, 4, " + ".join([str(i) for i in range(5)]), 10),
        ((5,), 15, expl_str, 5, " + ".join([str(i) for i in range(6)]), 15)
    )

    s2_tests =  (
        ((0,), 0, "the 0th triangular number is 0", ()),
        ((7,), 28, expl_str, 7, " + ".join([str(i) for i in range(8)]), 28),
        ((8,), 36, expl_str, 8, " + ".join([str(i) for i in range(9)]), 36),
        ((10,), 55, expl_str, 10, " + ".join([str(i) for i in range(11)]), 55),
        ((16,), 136, expl_str, 16, " + ".join([str(i) for i in range(17)]), 136),
        ((32,), 528, expl_str, 32, " + ".join([str(i) for i in range(33)]), 528),
        ((51,), 1326, expl_str, 51, " + ".join([str(i) for i in range(52)]), 1326),
        ((100,), 5050, expl_str, 100, " + ".join([str(i) for i in range(101)]), 5050)
    )

    def test_homework_2(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft1 = FunctionTestWithExplanation(fun, self.s1_tests,
                                          verbose = self.verbose - 1,
                                          raise_exceptions = self.raise_exceptions,
                                          suppress_output = _suppress_output)
        ft2 = FunctionTestWithExplanation(fun, self.s2_tests,
                                          verbose = self.verbose - 1,
                                          raise_exceptions = self.raise_exceptions,
                                          suppress_output = _suppress_output)
        st = StagedTest((ft1, ft2), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_2(False)
        print(msg)

    ## end Homework2Test


## To produce less verbose output, change 3 to 2 or 1:

Homework2Test("triangular.py", verbose = 3).run()

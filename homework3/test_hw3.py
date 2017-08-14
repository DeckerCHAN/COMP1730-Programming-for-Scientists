
import numpy

from testing import ModuleTestBase, FunctionTestWithExplanation, StagedTest

class Homework3Test (ModuleTestBase):

    fun_name = "total_days"

    tests = (
        ((1997, 2000), 1095, 'leap years: none'),
        ((1998, 2001), 1096, 'leap years: 2000'),
        ((1999, 2002), 1096, 'leap years: 2000'),
        ((2015, 2019), 1461, 'leap years: 2016'),
        ((2015, 2020), 1826, 'leap years: 2016'),
        ((2015, 2021), 2192, 'leap years: 2016, 2020'),
        ((1897, 1900), 1095, 'leap years: none'),
        ((1898, 1901), 1095, 'leap years: none'),
        ((1899, 1902), 1095, 'leap years: none'),
        ((0, 3), 1096, 'leap years: 0'),
        ((0, 4), 1461, 'leap years: 0'),
        ((0, 5), 1827, 'leap years: 0, 4'),
        ((-1, 4), 1826, 'leap years: 0')
    )

    def test_homework_3(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft = FunctionTestWithExplanation(fun, self.tests,
                                         type_cast_answer = False,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ok, msg = ft.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_3(False)
        print(msg)

    ## end Homework3Test


## To produce less verbose output, change 3 to 2 or 1:

Homework3Test("homework3.py", verbose = 3).run()

import logging
import time
import unittest

logging.basicConfig(filename="result.log", level=logging.INFO, format='%(levelname)s:%(message)s', filemode='w')
logger = logging.getLogger()
begin = time.time()
print(f" Program start at {begin}")


class Testarithmetic(unittest.TestCase):

    def test_1(self):
        with self.assertRaises(Exception):
            1 + '1'
        logger.warning("if value is not providing correct answer something is fishy here.")

    def test_square(self):
        num1 = 5
        result = num1 * num1
        self.assertEqual(result, 25)
        logger.exception("Value of number is double in this function. ")


    def test_cube(self):
        num2 = 3
        result = num2 ** 3
        self.assertTrue(result, 27)
        logger.info("Value is multiplied triple time in cube function ")



    def test_multiply(self):
        num3 = 2
        num4 = 6
        num5 = 7
        num6 = 8
        result = num3 * num4
        result1 = num5 * num6
        self.assertGreater(result1, result)
        logger.info(" Two results are compared after the multiplication that which one is greater")




end = time.time()
print(f"Program end at {end}")
print(f" Total running time of the program is {end - begin}")
if __name__ == '_main_':
    unittest.main()

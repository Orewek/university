import unittest
import filecmp
from pathlib import Path
from adjust_mas.adjust_mas_logic import clear_mas, len_mas
from kinda_task.task_logic import mean_arif, chered_checker, consecutive_result


class TestMas(unittest.TestCase):
    """
    just UnitTests
    """

    # ADJUST MAS BLOCK
    def test_clear_mas(self):
        mas = [213, 98213, 239, 8239, 999]
        mas_clear = clear_mas(mas)

        self.assertEqual(clear_mas, [])

    def test_len_mas(self):
        mas = [213, 98213, 239, 8239, 999]
        mas_len = len_mas(mas)
        
        self.assertEqual(mas_len, 5)
   
    # TASK MAS BLOCK
    def test_mean_arif(self):
        mas = [1, 2, 3, 4, 5, 6, 7]
        mas_mean_arif = mean_arif(mas)
        
        
        self.assertEqual(mas_mean_arif, 4)

    def test_chered_checker2(self):
        mas = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker2 = ''
        for i in range(len(mas)):
            result_chered_cheker2 += chered_checker(mas, len(mas), 2)
      
        self.assertEqual(result_chered_cheker2, '1010001')

    def test_chered_checker10(self):
        mas = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker10 = ''
        for i in range(len(mas)):
            result += chered_checker(mas, len(mas), 10)
      
        self.assertEqual(result_chered_cheker10, '1111101')

    def test_consecutive_result(self):
        mas = ['989', '213', '832', '932', '731', '84331', '232']
        result_mas = ['1', '1', '1', '1', '1', '0', '1']

        res1, res0 = consecutive_result(len(result_mas), result_mas)

        self.assertEqual(res1, 5)
        self.assertEqual(res0, 1)


if __name__ == '__main__':
    unittest.main()
    # python -m massive_laba.TestMas

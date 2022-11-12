import unittest

from adjust_mas.adjust_mas_logic import clear_mas, len_mas

from input_mas.input_mas_logic import generate_el

from kinda_task.task_logic import chered_checker, consecutive_result, mean_arif


class TestMas(unittest.TestCase):
    """
    just UnitTests
    """

    # ADJUST MAS BLOCK
    def test_clear_mas(self) -> None:
        mas = [213, 98213, 239, 8239, 999]
        mas_clear = clear_mas(mas)

        self.assertEqual(mas_clear, [])

    def test_len_mas(self) -> None:
        mas = [213, 98213, 239, 8239, 999]
        mas_len = len_mas(mas)

        self.assertEqual(mas_len, '5 - length of massive')

    # TASK MAS BLOCK
    """
    def test_mean_arif(self):
        mas = [1, 2, 3, 4, 5, 6, 7]
        mas_mean_arif = mean_arif(mas)

        self.assertEqual(mas_mean_arif, 4)
    """

    def test_chered_checker2(self) -> None:
        mas = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker2 = ''
        for i in range(len(mas)):
            result_chered_cheker2 += chered_checker(int(mas[i]), 2)

        self.assertEqual(result_chered_cheker2, '1010001')

    def test_chered_checker10(self) -> None:
        mas = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker10 = ''
        for i in range(len(mas)):
            result_chered_cheker10 += chered_checker(int(mas[i]), 10)

        self.assertEqual(result_chered_cheker10, '1111101')

    def test_consecutive_result(self) -> None:
        result_mas = ['1', '1', '1', '1', '1', '0', '1']

        res1, res0 = consecutive_result(result_mas)

        self.assertEqual(res1, 5)
        self.assertEqual(res0, 1)

    def test_generate_el(self) -> None:
        mas = generate_el(mas=[], amount_elements=5)

        ok = 1
        if len(mas) > 0:
            for i in range(len(mas)):
                if mas[i] is None:
                    ok = 0
                    break

        self.assertAlmostEqual(ok, 1)


if __name__ == '__main__':
    unittest.main()
    # python -m Unit_tests.unit_test

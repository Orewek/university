# -*- coding: utf-8 -*-
"""Unitests."""

import unittest

from adjust_mas.adjust_mas_logic import clear_mas, len_mas

from input_mas.input_mas_logic import generate_el

from kinda_task.task_logic import chered_checker, consecutive_result


class TestMas(unittest.TestCase):
    """Just UnitTests."""

    # ADJUST MAS BLOCK
    def test_clear_mas(self: self) -> None:
        """Check clear mas."""
        mas: list = [213, 98213, 239, 8239, 999]
        mas_clear = clear_mas(mas)

        self.assertEqual(mas_clear, []) # act

    def test_len_mas(self: self) -> None:
        """Check len_mas."""
        mas: list = [213, 98213, 239, 8239, 999]
        mas_len: int = len_mas(mas)

        self.assertEqual(mas_len, '5 - length of massive') # act

    # TASK MAS BLOCK
    def test_chered_checker2(self: self) -> None:
        """Check chered_checker2."""
        mas: list = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker2: str = ''.join(chered_checker(int(mas[i]), 2) for i in range(len(mas)))

        self.assertEqual(result_chered_cheker2, '1010001') # act

    def test_chered_checker10(self: self) -> None:
        """Check chered_checker10."""
        mas: list = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker10: str = ''.join(chered_checker(int(mas[i]), 10) for i in range(len(mas)))

        self.assertEqual(result_chered_cheker10, '1111101') # act

    def test_consecutive_result(self: self) -> None:
        """Check concecutive_result."""
        result_mas: list = ['1', '1', '1', '1', '1', '0', '1']
        res1, res0 = consecutive_result(result_mas)

        self.assertEqual((res0, res1), (1, 5)) # act

    def test_generate_el(self: self) -> None:
        """Check generate el."""
        mas: list = generate_el(mas=[], amount_elements=5)
        ok: int = 1
        if len(mas) > 0:
            ok = all(mas[i] is not None for i in range(len(mas)))

        self.assertAlmostEqual(ok, 1) # act


if __name__ == '__main__':
    unittest.main()
    # python -m Unit_tests.unit_test

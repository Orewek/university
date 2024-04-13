## Юнит-тесты

### Обычные юнит тесты, проверяют работу логических функций

```py
    def test_clear_mas(self) -> None:
        mas: list = [213, 98213, 239, 8239, 999]
        mas_clear = clear_mas(mas)

        self.assertEqual(mas_clear, [])
```
```py
    def test_len_mas(self) -> None:
        mas: list = [213, 98213, 239, 8239, 999]
        mas_len: int = len_mas(mas)

        self.assertEqual(mas_len, 5)
```
```py
    def test_mean_arif(self) -> None:
        mas: list = [1, 2, 3, 4, 5, 6, 7]
        mas_mean_arif: float = mean_arif(mas)

        self.assertEqual(mas_mean_arif, 4)
```
```py
    def test_chered_checker2(self) -> None:
        mas: list = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker2: str = ''
        for i in range(len(mas)):
            result_chered_cheker2 += chered_checker(mas, len(mas), 2)

        self.assertEqual(result_chered_cheker2, '1010001')
```
```py
    def test_chered_checker10(self) -> None:
        mas: list = ['989', '213', '832', '932', '731', '84331', '232']
        result_chered_cheker10 = ''
        for i in range(len(mas)):
            result_chered_cheker10 += chered_checker(mas, len(mas), 10)

        self.assertEqual(result_chered_cheker10, '1111101')
```
```py
    def test_consecutive_result(self) -> None:
        result_mas: list = ['1', '1', '1', '1', '1', '0', '1']

        res1, res0 = consecutive_result(len(result_mas), result_mas)

        self.assertEqual(res1, 5)
        self.assertEqual(res0, 1)
```
```py
    def test_generate_el(self) -> None:
        mas: list = generate_el(mas=[], amount_elements=5)

        ok: int = 1
        if len(mas) > 0:
            for i in range(len(mas)):
                if mas[i] is None:
                    ok: int = 0
                    break

        self.assertAlmostEqual(OK, 1)
```
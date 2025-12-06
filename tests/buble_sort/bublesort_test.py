from Package.buble_sort.bublesort import bubble_sort


class TestBubbleSort:
    def test_sort_regular_list(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert bubble_sort(arr) == expected

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == expected

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == expected

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 1]
        expected = [1, 2, 2, 5, 5, 8]
        assert bubble_sort(arr) == expected

    def test_empty_list(self):
        arr = []
        expected = []
        result = bubble_sort(arr)
        assert result == expected

    def test_single_element(self):
        arr = [42]
        expected = [42]
        assert bubble_sort(arr) == expected

    def test_negative_numbers(self):
        arr = [-5, 2, -8, 0, 3, -1]
        expected = [-8, -5, -1, 0, 2, 3]
        assert bubble_sort(arr) == expected

    def test_large_list(self):
        arr = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        result = bubble_sort(arr)
        assert result == expected

    def test_all_equal_elements(self):
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        assert bubble_sort(arr) == expected

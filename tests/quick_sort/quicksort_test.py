from Package.quick_sort.quicksort import quicksort
import pytest
class TestQuickSort:
    
    def test_sort_regular_list(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert quicksort(arr) == expected
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        assert quicksort(arr) == expected
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert quicksort(arr) == expected
    
    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 1]
        expected = [1, 2, 2, 5, 5, 8]
        assert quicksort(arr) == expected
    
    def test_negative_numbers(self):
        arr = [-5, 2, -8, 0, 3, -1]
        expected = [-8, -5, -1, 0, 2, 3]
        assert quicksort(arr) == expected
    
    def test_large_list(self):
        arr = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        result = quicksort(arr)
        assert result == expected
    
    
    def test_all_equal_elements(self):
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        assert quicksort(arr) == expected
    
    def test_float_numbers(self):
        arr = [3.5, 1.2, 4.8, 2.1, 0.5]
        expected = [0.5, 1.2, 2.1, 3.5, 4.8]
        result = quicksort(arr)
        assert result == expected
    
    def test_odd_number_of_elements(self):
        arr = [3, 1, 4, 1, 5]
        expected = [1, 1, 3, 4, 5]
        assert quicksort(arr) == expected
    
    def test_even_number_of_elements(self):
        arr = [3, 1, 4, 1]
        expected = [1, 1, 3, 4]
        assert quicksort(arr) == expected
    
    def test_with_strings_should_fail(self):
        arr = [3, "2", 1]
        with pytest.raises(TypeError):
            quicksort(arr)
    
    def test_quick_sort_with_pivot_at_end(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        assert quicksort(arr) == expected
    
    def test_quick_sort_with_worst_case(self):
      
        arr = list(range(100))
        expected = list(range(100))
        result = quicksort(arr)
        assert result == expected




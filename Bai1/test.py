import os
import copy
from random import randint
from unittest import TestCase
from datetime import datetime
from src.file import parallel_write_file
from src.sort import parallel_quick_sort
from collections import Counter


def assertExist(path):
    if not os.path.exists(path):
        print("FAIL: Not exists folder.")


class TestFile(TestCase):

    def assertFile(self, path, expected):
        assertExist(path)
        num_files = expected[0]
        num_threads = expected[-1]
        list_file = os.listdir(path)
        if len(list_file) != num_files:
            self.assertEqual(len(list_file), num_files, msg="Not enough number of files")
        thread = []
        for file in list_file:
            file = str(file).split("_")
            thread.append(file[1])
        thread = Counter(thread)
        if len(thread) != num_threads:
            self.assertEqual(len(thread), num_threads, msg="Not enough number of threads")

    def test_write_file(self):
        time = datetime.today()
        time = str(time).replace(" ", "_")
        time = time[:-1]
        parallel_write_file(time, 10, 100, 10)
        current_path = os.getcwd()
        path = os.path.join(current_path, time)
        self.assertFile(path, [10, 10])

    def test_sorted(self):
        arr = [randint(-100, 100) for _ in range(1000)]
        temp = sorted(arr)
        parallel_quick_sort(arr, 2)
        self.assertListEqual(temp, arr, msg="Parallel quick sort function not true.")


def main():
    pass


if __name__ == '__main__':
    main()

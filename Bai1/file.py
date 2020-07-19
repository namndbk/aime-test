from random import randint
import time
import os
import sys
import threading
from sort import parallel_quick_sort


def assert_dir(folder_name):
    current_path = os.getcwd()
    folder_path = os.path.join(current_path, folder_name)
    if not os.path.exists(folder_path):
        print("Error: {} does not exist.".format(folder_path))
        return 1
    if not os.path.isdir(folder_path):
        print("Error: {} is not directory.".format(folder_path))
        return 0
    return 2


def write_file(folder_name, num_files, length, thread_name=None):
    for i in range(num_files):
        if thread_name is not None:
            file_name = folder_name + "/" + "{}_{}.txt".format(thread_name, i + 1)
        else:
            file_name = folder_name + "/" + "{}.txt".format(i + 1)
        arr = [randint(-1e6, 1e6) for _ in range(length)]
        arr = sorted(arr)
        with open(file_name, "w", encoding="utf-8") as f:
            for j in range(length):
                f.write(str(arr[j]) + "\n")
        del arr


def read_file(file_name):
    results = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    results.append(int(line.strip()))
        return results
    except Exception as e:
        raise e


class ThreadFileLoader(threading.Thread):
    def __init__(self, list_file, list_lock, out_lock, arr):
        threading.Thread.__init__(self)
        self._list_file = list_file
        self._list_lock = list_lock
        self._out_lock = out_lock
        self._arr = arr

    def run(self):
        while True:
            self._list_lock.acquire()
            try:
                file_name = self._list_file.pop()
            except IndexError:
                raise IndexError("List file is empty")
            finally:
                self._list_lock.release()
            self._out_lock.acquire()
            self._arr += read_file(file_name)
            self._out_lock.release()


def parallel_read_file(folder_name, num_threads=None):
    """
    :param folder_name: folder name
    :param num_threads: number of threads
    :return:
    """
    list_lock = threading.Lock()
    out_lock = threading.Lock()
    arr = []
    threads = []
    if num_threads is None:
        try:
            num_threads = os.cpu_count()
        except AttributeError:
            num_threads = 4
    elif num_threads < 1:
        raise ValueError("Num_thread must be > 0")
    current_path = os.getcwd()
    list_file = []
    folder_path = os.path.join(current_path, folder_name)
    if assert_dir(folder_path) != 2:
        print("Please, check folder path")
        sys.exit(1)
    files = os.listdir(folder_path)
    for file_name in files:
        file_name = os.path.join(folder_path, file_name)
        list_file.append(file_name)
    for i in range(num_threads):
        thread = ThreadFileLoader(list_file, list_lock, out_lock, arr)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return arr


def parallel_write_file(folder_name, n_files, length, num_threads):
    """
    :param folder_name: directory name
    :param n_files: number of files to save
    :param length: n_number in each file
    :param num_threads: number of thread
    :return:
    """
    current_path = os.getcwd()
    folder_path = os.path.join(current_path, folder_name)
    if assert_dir(folder_path) == 1:
        try:
            print("Creating new folder ...")
            os.mkdir(folder_path)
        except OSError:
            print("Creation of the directory %s failed" % folder_path)
            sys.exit(1)
        else:
            print("Successfully created the directory %s " % folder_path)
    if num_threads is None:
        try:
            num_threads = os.cpu_count()
        except AttributeError:
            num_threads = 4
    elif num_threads < 1:
        raise ValueError("Num_threads must be > 0")
    for i in range(num_threads):
        num_files = n_files // num_threads
        thread_name = "thread_{}".format(i + 1)
        write_file(folder_name, num_files, length, thread_name)


def merge_file(folder_name, file_name, num_threads):
    arr = parallel_read_file(folder_name, num_threads=num_threads)
    parallel_quick_sort(arr, 2)
    with open(file_name, "w", encoding="utf-8") as f:
        for x in arr:
            f.write(str(x) + "\n")
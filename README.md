# Ý tưởng giải quyết các bài toán


## Bài 1
- Để sinh dữ liệu, chạy hàm parallel_write_file trong file file.py.

- Unit test viết ở file test.py

- Các hàm sort viết ở file sort.py

- Để merger file, chạy hàm merge_file trong file.py. Lưu ý, số lượng thread trong hàm này phải là lũy thừa của 2

- Ý tưởng cho thuật toán parallel_quick_sort
    Thuật tóan quick sort dựa trên ý tưởng chia để trị, chia một dãy con thành 2 dãy nhỏ hơn, bên trái nhỏ hơn bằng pivot, bên phải lớn hơn pivot. Sau đó gọi đệ quy trên hai dãy đó. Điểm neo đệ quy là dãy không thể phân chia hoặc đủ nhỏ để sử dụng thuật toán sắp xếp đơn giản hơn, ví dụ như selection sort

    Vậy nên, thay vì cứ liên tục phân chia dãy, ta chỉ chia n lần, khi đó ta được 2^n dãy con. Mỗi dãy sử dụng một thread để sắp xếp.



## Bài 2
- Có thể bắt các năm từ 1 - 2999. Định dạng năm-tháng-ngày có thể thay "-" bởi / hoặc .



## Bài 3
### Ý tưởng thuật toán
- B1. Ta đi tìm điểm giữa của dãy liên kết đơn, bằng cách sử dụng 2 con trỏ có bước nhảy khác nhau. Sau đó cắt dãy thành 2 dãy liên kết đơn tại điểm giữa đó.
    Độ phức tạp về thời gian là O(n), với bộ nhớ thì chỉ sử dụng thêm vài biến phụ.

- B2. Với dãy sau (dãy từ điểm giữa đổ về cuối), ta tiến hành đảo ngược. Độ phức tạp về thời gian là O(n), với bộ nhớ thì chỉ sử dụng thêm vài biến phụ.

- B3. Trộn hai dãy với nhau, ta được dãy cần tìm. Độ phức tạp về thời gian là O(n), với bộ nhớ thì chỉ sử dụng thêm vài biến phụ.

    Tổng kết: độ phức tạp về thời gian là O(n), độ phức tạp bộ nhớ O(1)

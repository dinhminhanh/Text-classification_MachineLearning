HƯỚNG DẪN CÀI ĐẶT, BIÊN DỊCH VÀ CHẠY CHƯƠNG TRÌNH TỪ FILE `main.ipynb`

1. Yêu cầu hệ thống
   - Python: Phiên bản 3.8 trở lên.
   - Hệ điều hành: Windows, macOS, hoặc Linux.
   - Jupyter Notebook: Dùng để chạy file `main.ipynb`.

2. Các thư viện và gói phần mềm cần thiết
   - numpy: Xử lý số học và mảng đa chiều.
   - scikit-learn: Thuật toán học máy (Naive Bayes, SVM, Logistic Regression).
   - pyvi: Thư viện hỗ trợ tách từ tiếng Việt.
   - matplotlib: Vẽ đồ thị.
   - seaborn: Biểu đồ trực quan.
   - json: Xử lý dữ liệu JSON.

3. Tệp tin yêu cầu
   - vietnamese-stopwords.txt: Danh sách từ dừng tiếng Việt.
   - Thư mục `json`: Chứa tệp dữ liệu định dạng JSON.

4. Cài đặt
   4.1. Cài đặt Python
        - Tải Python tại: https://www.python.org/downloads/
        - Cài đặt và chọn "Add Python to PATH".

   4.2. Cài đặt thư viện
        - Mở Command Prompt/Terminal, điều hướng đến thư mục `main.ipynb`.
        - Chạy lệnh:
          pip install numpy scikit-learn pyvi matplotlib seaborn jupyter

   4.3. Cài đặt Jupyter Notebook
        - Nếu chưa có, chạy lệnh:
          pip install notebook

5. Hướng dẫn chạy chương trình
   5.1. Chuẩn bị dữ liệu
        - Tạo thư mục `json` cùng vị trí với file `main.ipynb`.
        - Đặt các file JSON dữ liệu vào thư mục này.
        - Đảm bảo file `vietnamese-stopwords.txt` có trong thư mục.

   5.2. Mở và chạy chương trình
        - Mở Terminal/Command Prompt.
        - Điều hướng tới thư mục chứa file `main.ipynb`.
        - Chạy lệnh:
          jupyter notebook
        - Trong giao diện Jupyter Notebook:
          + Mở file `main.ipynb`.
          + Chạy các cell theo thứ tự.

   5.3. Kết quả đầu ra
        - Độ chính xác: Tập huấn luyện và kiểm tra.
        - Báo cáo phân loại: Precision, Recall, F1-score, Accuracy.
        - Dự đoán nhãn: Hiển thị từ mô hình.
        - Biểu đồ: Phân phối dữ liệu trực quan.

6. Mô tả các mô hình
   - Naive Bayes: Sử dụng `GaussianNB` để phân loại văn bản.
   - SVM: Sử dụng `SVC` với kernel tuyến tính để phân loại.
   - Logistic Regression: Sử dụng `LogisticRegression` cho bài toán phân loại đa lớp.

7. Ghi chú
   - Kiểm tra cài đặt đầy đủ thư viện trước khi chạy.
   - Kiểm tra cấu trúc file JSON và từ dừng.
   - Đảm bảo dữ liệu đủ lớn và cân bằng giữa các lớp.



# Thuật toán SVM dùng trong Text Classification với thư viện Scikit-learn

## 1. Thư viện Scikit-learn  

Scikit-learn (viết tắt là Sklearn) là một thư viện mã nguồn mở dành cho Machine Learning - một ngành trong trí tuệ nhân tạo, rất mạnh mẽ và thông dụng với cộng đồng Python, được thiết kế trên nền NumPy và SciPy. Scikit-learn chứa hầu hết các thuật toán Machine Learning hiện đại nhất, đi kèm với documentations luôn được cập nhật.

Tại sao chọn thư viện Scikit-learn để giải quyết bài toán này?  

- Hỗ trợ các thuật toán tối ưu cho bài toán phân loại, bao gồm SVM với nhiều kernel khác nhau.
- Giao diện đơn giản, dễ sử dụng và tích hợp các công cụ mạnh mẽ để xử lý tiền xử lý dữ liệu, xây dựng pipeline, đánh giá mô hình.
- Độ tin cậy cao do Scikit-learn được xây dựng bởi các chuyên gia hàng đầu.
- Có nguồn dữ liệu phong phú như iris, digit, …, rất tiện lợi để thử nghiệm và nghiên cứu.

## 2. Thuật toán SVM  

### 2.1. Định nghĩa  

**Support Vector Machine (SVM)** là một thuật toán học có giám sát (Supervised Learning) được sử dụng phổ biến cho các bài toán phân loại và hồi quy. SVM hoạt động bằng cách tìm một siêu phẳng (hyperplane) tối ưu để phân tách các điểm dữ liệu thuộc các lớp khác nhau trong không gian đặc trưng.

#### Đặc điểm nổi bật:

- SVM có thể áp dụng tốt cho cả bài toán phân loại tuyến tính và phi tuyến tính.
- Thuật toán này sử dụng một hàm kernel để ánh xạ dữ liệu gốc sang không gian đặc trưng cao hơn, từ đó làm tăng khả năng phân tách các lớp phức tạp.

### 2.2. Thành phần chính của SVM  

1. **Siêu phẳng tối ưu**: Siêu phẳng được xác định sao cho khoảng cách từ các điểm dữ liệu gần nhất (support vectors) đến siêu phẳng này là lớn nhất.
2. **Support Vectors**: Là các điểm dữ liệu gần siêu phẳng nhất và có vai trò quyết định trong việc xác định siêu phẳng.
3. **Hàm kernel**: Ánh xạ dữ liệu từ không gian gốc lên không gian đặc trưng cao hơn. Một số hàm kernel phổ biến:
   - Linear Kernel: Sử dụng cho dữ liệu có thể phân tách tuyến tính.
   - Polynomial Kernel: Dùng cho dữ liệu phi tuyến tính với các mối quan hệ phức tạp.
   - RBF (Radial Basis Function): Phổ biến nhất, dùng cho dữ liệu phi tuyến.

### 2.3. Đánh giá  

#### Ưu điểm:
- SVM hiệu quả với dữ liệu có độ nhiễu thấp, phù hợp với dữ liệu nhiều chiều (high-dimensional).
- Hoạt động tốt với bài toán phân loại nhị phân và đa lớp.
- Khả năng tổng quát hóa tốt, đặc biệt với dữ liệu nhỏ và phức tạp.

#### Nhược điểm:
- Chi phí tính toán cao đối với tập dữ liệu lớn, do thời gian huấn luyện tăng theo kích thước dữ liệu.
- Cần chọn lựa hàm kernel và tham số (hyperparameters) phù hợp để đạt hiệu quả cao.

### 2.4. Sử dụng SVM trong Text Classification  

Trong bài toán phân loại văn bản, SVM thường sử dụng **RBF kernel** hoặc **linear kernel** để xử lý dữ liệu văn bản đã được chuyển đổi thành vector thông qua các phương pháp như **TF-IDF** hoặc **Bag of Words**. Với dữ liệu văn bản, kernel tuyến tính thường được ưa chuộng hơn vì dữ liệu thường nằm trong không gian cao và dễ dàng phân tách tuyến tính.

References:  

1. https://scikit-learn.org/stable/modules/svm.html  
2. https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html  
3. https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html  

Dưới đây là nội dung giới thiệu **Logistic Regression** theo cấu trúc bạn cung cấp:

---

# Thuật toán Logistic Regression dùng trong Text Classification với thư viện Scikit-learn  

## 1. Thư viện Scikit-learn  

Scikit-learn (viết tắt là Sklearn) là một thư viện mã nguồn mở dành cho Machine Learning - một ngành trong trí tuệ nhân tạo, rất mạnh mẽ và thông dụng với cộng đồng Python, được thiết kế trên nền NumPy và SciPy. Scikit-learn chứa hầu hết các thuật toán Machine Learning hiện đại nhất, đi kèm với documentations luôn được cập nhật.

Tại sao chọn thư viện Scikit-learn để giải quyết bài toán này?  

- Hỗ trợ thuật toán Logistic Regression với giao diện thân thiện và dễ sử dụng.  
- Cung cấp công cụ để tinh chỉnh tham số của Logistic Regression, chẳng hạn như **regularization** (L1, L2).  
- Tích hợp sẵn các công cụ tiền xử lý dữ liệu, giúp chuẩn hóa và mã hóa dữ liệu dễ dàng.  
- Tài liệu đầy đủ, minh họa chi tiết, và có độ tin cậy cao.  
- Thích hợp để xây dựng pipeline cho bài toán phân loại văn bản.  

## 2. Thuật toán Logistic Regression  

### 2.1. Định nghĩa  

**Logistic Regression** là một thuật toán phân loại thuộc nhóm học có giám sát (Supervised Learning). Mặc dù tên gọi có chữ "Regression", Logistic Regression không phải là thuật toán hồi quy mà là thuật toán phân loại, chủ yếu được sử dụng để dự đoán xác suất một mẫu thuộc về một lớp cụ thể.

Logistic Regression hoạt động dựa trên hàm sigmoid (logistic function):  

\[
h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}
\]

Hàm sigmoid ánh xạ giá trị dự đoán của mô hình vào khoảng \([0, 1]\), từ đó chuyển đổi bài toán dự đoán tuyến tính thành bài toán phân loại.

### 2.2. Thành phần chính  

1. **Hàm mục tiêu (Loss Function)**: Logistic Regression sử dụng hàm mất mát log-likelihood:  

\[
L(\theta) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]
\]

2. **Regularization**: Để tránh hiện tượng overfitting, thuật toán Logistic Regression tích hợp hai loại regularization:  
   - **L1 regularization**: Làm giảm số lượng trọng số không cần thiết (sparse model).  
   - **L2 regularization**: Làm giảm độ lớn của các trọng số, giúp mô hình ổn định hơn.

3. **Optimization**: Logistic Regression sử dụng các thuật toán tối ưu hóa như **Gradient Descent** hoặc **Quasi-Newton Method (BFGS)**.

### 2.3. Đánh giá  

#### Ưu điểm:
- Đơn giản, dễ hiểu và dễ triển khai.
- Hiệu quả với dữ liệu lớn và có tính tuyến tính cao.
- Thích hợp cho cả bài toán nhị phân và phân loại đa lớp (sử dụng kỹ thuật one-vs-rest hoặc softmax).
- Khả năng giải thích tốt nhờ mối quan hệ tuyến tính giữa đặc trưng và kết quả.

#### Nhược điểm:
- Hiệu suất thấp khi dữ liệu không tuyến tính (không thể phân tách tuyến tính).
- Nhạy cảm với các outlier, cần xử lý tiền xử lý kỹ lưỡng.

### 2.4. Sử dụng Logistic Regression trong Text Classification  

Logistic Regression thường được sử dụng để phân loại văn bản nhờ vào tính đơn giản và khả năng mở rộng tốt. Các bước cơ bản:  

1. Chuyển đổi dữ liệu văn bản thành vector (TF-IDF hoặc Bag of Words).  
2. Chuẩn hóa dữ liệu (StandardScaler) nếu cần.  
3. Huấn luyện Logistic Regression với regularization L2 (thường là lựa chọn mặc định).  
4. Sử dụng các công cụ như **GridSearchCV** để tối ưu các tham số như `C` (strength of regularization).  

References:  

1. https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression  
2. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html  
3. https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html  


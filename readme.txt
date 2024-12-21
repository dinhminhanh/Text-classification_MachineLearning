**HƯỚNG DẪN CÀI ĐẶT, BIÊN DỊCH VÀ CHẠY CHƯƠNG TRÌNH TỪ FILE `main.ipynb`**

---

### **1. Yêu cầu hệ thống**
- **Python:** Phiên bản 3.8 trở lên.
- **Hệ điều hành:** Windows, macOS, hoặc Linux.
- **Jupyter Notebook:** Dùng để chạy file `main.ipynb`.

---

### **2. Các thư viện và gói phần mềm cần thiết**
- **numpy:** Xử lý số học và mảng đa chiều.
- **scikit-learn:** Cung cấp các thuật toán học máy như Naive Bayes, SVM, Logistic Regression, và các công cụ xử lý dữ liệu.
- **pyvi:** Thư viện hỗ trợ tách từ tiếng Việt.
- **matplotlib:** Thư viện vẽ đồ thị.
- **seaborn:** Hỗ trợ biểu đồ và hiển thị dữ liệu.
- **json:** Đọc và xử lý dữ liệu JSON.

---

### **3. Tệp tin yêu cầu**
1. **vietnamese-stopwords.txt:** Danh sách từ dừng tiếng Việt.
2. **Thư mục `json`:** Chứa các tệp dữ liệu định dạng JSON.

---

### **4. Cài đặt**

#### **4.1. Cài đặt Python**
1. Tải Python từ [trang chính thức](https://www.python.org/downloads/).
2. Cài đặt Python và đảm bảo tích chọn **Add Python to PATH** trong quá trình cài đặt.

#### **4.2. Cài đặt các thư viện**
1. Mở **Command Prompt** (Windows) hoặc **Terminal** (macOS/Linux).
2. Điều hướng đến thư mục chứa file `main.ipynb` và chạy lệnh:
   ```bash
   pip install numpy scikit-learn pyvi matplotlib seaborn jupyter
   ```

#### **4.3. Cài đặt Jupyter Notebook**
1. Nếu chưa có Jupyter Notebook, cài đặt bằng lệnh:
   ```bash
   pip install notebook
   ```

---

### **5. Hướng dẫn chạy chương trình**

#### **5.1. Chuẩn bị dữ liệu**
1. Tạo thư mục `json` trong cùng thư mục với file `main.ipynb`.
2. Đặt các file JSON dữ liệu vào thư mục này.
3. Đảm bảo file `vietnamese-stopwords.txt` có trong cùng thư mục với `main.ipynb`.

#### **5.2. Mở và chạy chương trình**
1. Mở **Command Prompt** hoặc **Terminal**.
2. Điều hướng đến thư mục chứa file `main.ipynb`.
3. Chạy Jupyter Notebook bằng lệnh:
   ```bash
   jupyter notebook
   ```
4. Trong giao diện Jupyter Notebook, mở file `main.ipynb`.
5. Chạy từng ô lệnh (**cell**) theo thứ tự để thực thi chương trình.

#### **5.3. Kết quả đầu ra**
- **Độ chính xác:** Hiển thị độ chính xác cho tập huấn luyện và kiểm tra.
- **Báo cáo phân loại:** Gồm các chỉ số:
  - **Precision, Recall, F1-score, Accuracy.**
- **Dự đoán nhãn:** Hiển thị nhãn dự đoán từ các mô hình.
- **Biểu đồ phân phối dữ liệu:** Hiển thị trực quan phân phối nhãn dữ liệu.

---

### **6. Mô tả các mô hình sử dụng**
- **Naive Bayes:**
  - Sử dụng `GaussianNB` để phân loại văn bản.
- **SVM (Support Vector Machine):**
  - Sử dụng `SVC` với kernel tuyến tính để phân loại.
- **Logistic Regression:**
  - Sử dụng `LogisticRegression` cho bài toán phân loại đa lớp.

---

### **7. Ghi chú**
- Đảm bảo các thư viện đã được cài đặt đầy đủ trước khi chạy chương trình.
- Trong trường hợp xảy ra lỗi:
  1. Kiểm tra cấu trúc tệp JSON và file danh sách từ dừng.
  2. Đảm bảo dữ liệu đủ lớn và cân bằng giữa các lớp để cải thiện hiệu quả mô hình.

--- 


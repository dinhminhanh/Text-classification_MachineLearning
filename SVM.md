# Tìm hiểu về Số Chu Kỳ Tập Luyện SVM và Các Hiện Tượng Liên Quan

## **1. Chu Kỳ Tập Luyện SVM**

Mặc định, mô hình SVM (`SVC`) trong thư viện scikit-learn không có tham số trực tiếp để giới hạn số chu kỳ tập luyện vì thuật toán tìm nghiệm không dựa trên các epoch như các mô hình gradient descent.

Tuy nhiên, bạn có thể giới hạn số chu kỳ (hoặc số lần lặp) bằng cách đặt tham số `max_iter` khi khởi tạo `SVC`. Ví dụ:

```python
models = {
    "SVM": SVC(kernel='linear', max_iter=1000)  # Giới hạn số lần lặp tối đa là 1000
}
```

### **Mặc định:**
- Nếu không đặt `max_iter`, SVM sẽ chạy đến khi hội tụ (convergence). Điều này có thể tốn thời gian với dữ liệu lớn hoặc phức tạp.

### **Kiểm tra số lần lặp thực tế:**
- Bạn có thể đặt `verbose=True` khi khởi tạo SVM để theo dõi quá trình tối ưu. Tuy nhiên, việc này sẽ in ra rất nhiều thông tin chi tiết.

---

## **2. Hiện Tượng "Nhiều Âm Lên Dương Không Đổi"**

Hiện tượng này xảy ra khi giá trị của hàm mục tiêu hoặc các tham số của mô hình thay đổi không ổn định qua các chu kỳ huấn luyện. Trong bài toán SVM, các nguyên nhân và hiện tượng cụ thể bao gồm:

### **2.1. Hiện Tượng Trong Quá Trình Hội Tụ**

#### **Nguyên Nhân:**
- Dữ liệu có nhiễu hoặc không tuyến tính, không thể phân tách tốt bằng đường thẳng hoặc mặt phẳng trong không gian đặc trưng.
- Tham số không phù hợp, ví dụ `C` hoặc `gamma` được chọn không chính xác.

#### **Hiện Tượng:**
- Giá trị hàm mục tiêu dao động và không đạt trạng thái hội tụ.
- Nếu `max_iter` quá thấp, mô hình không hội tụ trước khi kết thúc.
- Nếu không giới hạn `max_iter`, quá trình huấn luyện có thể kéo dài rất lâu.

---

### **2.2. Hiện Tượng Tối Ưu Không Thành Công**

#### **Nguyên Nhân:**
- Dữ liệu bị lệch (skewed data) hoặc không tuyến tính nghiêm trọng.
- Với `kernel='linear'`, dữ liệu phi tuyến không thể được phân loại tốt, cần sử dụng kernel khác như `rbf` hoặc `poly`.

#### **Hiện Tượng:**
- Độ chính xác thấp và không ổn định.
- Sai số hội tụ lớn, dẫn đến phân loại kém trên tập kiểm tra.

---

### **2.3. Hiện Tượng Overfitting hoặc Underfitting**

#### **Nguyên Nhân:**
- Tham số `C` không được điều chỉnh tốt:
  - `C` lớn: Mô hình cố gắng phân tách hoàn toàn dữ liệu huấn luyện, dẫn đến quá khớp (overfitting).
  - `C` nhỏ: Mô hình chấp nhận nhiều lỗi trong huấn luyện, dẫn đến phân loại kém (underfitting).

#### **Hiện Tượng:**
- **Overfitting:** Hiệu suất tốt trên tập huấn luyện nhưng kém trên tập kiểm tra.
- **Underfitting:** Hiệu suất kém cả trên tập huấn luyện và tập kiểm tra.

---

## **3. Cách Xử Lý và Kiểm Tra Hiện Tượng**

### **3.1. Kiểm Tra Log Quá Trình Huấn Luyện**
- Sử dụng `verbose=True` để theo dõi giá trị hàm mục tiêu qua các chu kỳ.
- Nếu giá trị không thay đổi hoặc dao động nhiều, cần điều chỉnh tham số.

### **3.2. Điều Chỉnh Tham Số SVM**
- **Thay đổi kernel:**
  - Sử dụng `rbf`, `poly` thay vì `linear` nếu dữ liệu không tuyến tính.
- **Điều chỉnh `C`:**
  - Thử nghiệm với các giá trị từ nhỏ đến lớn bằng `GridSearchCV` hoặc `RandomizedSearchCV`.
- **Giới hạn `max_iter`:**
  - Đặt giá trị hợp lý để tránh quá trình tối ưu kéo dài.

### **3.3. Chuẩn Hóa Dữ Liệu**
- Sử dụng `StandardScaler` để chuẩn hóa các đặc trưng về cùng một phạm vi giá trị, giảm ưu thế của các đặc trưng có giá trị lớn hơn.

### **3.4. Kiểm Tra và Cải Thiện Dữ Liệu**
- Loại bỏ hoặc giảm nhiễu dữ liệu nếu có.
- Tăng số lượng mẫu nếu dữ liệu mất cân bằng.

---

## **4. Kết Luận**
- **Chu kỳ tập luyện SVM** có thể được kiểm soát thông qua tham số `max_iter`, nhưng cần cẩn thận để đảm bảo mô hình hội tụ đúng cách.
- Để tránh hiện tượng "nhiều âm lên dương không đổi", cần kiểm tra dữ liệu và điều chỉnh tham số phù hợp.
- Nếu dữ liệu không tuyến tính hoặc bị nhiễu, các kernel phi tuyến như `rbf` hoặc `poly` có thể là lựa chọn tốt hơn.

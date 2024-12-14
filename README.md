# Phân loại văn bản với PCA và Naive Bayes

Dự án này minh họa cách thực hiện phân loại văn bản sử dụng các kỹ thuật học máy, bao gồm tiền xử lý văn bản, giảm chiều với PCA (Phân tích Thành phần Chính), và huấn luyện mô hình phân loại Naive Bayes.
## Mục lục
1. [Giới thiệu](#giới-thiệu)
2. [Thư viện](#thư-viện)
3. [Tiền xử lý dữ liệu](#tiền-xử-lý-dữ-liệu)
4. [Mô hình](#mô-hình)
5. [Chạy chương trình](#chạy-chương-trình)


## Giới thiệu
Dự án này triển khai một hệ thống phân loại văn bản xử lý các tài liệu tiếng Việt ở định dạng JSON, sử dụng phương pháp TF-IDF (Term Frequency-Inverse Document Frequency) để biểu diễn dữ liệu văn bản, giảm chiều không gian đặc trưng bằng PCA, và phân loại dữ liệu bằng các bộ phân loại Naive Bayes. Mục tiêu của mô hình là dự đoán danh mục (nhãn) của mỗi tài liệu.

Mô hình phân loại được đánh giá thông qua các điểm số độ chính xác trên cả tập huấn luyện và tập kiểm tra.

## Thư viện
Để chạy dự án này, bạn cần cài đặt các thư viện Python sau:

- `numpy`
- `scikit-learn`
- `pyvi`
- `json`
- `os`
- `matplotlib`
- `seaborn`

Bạn có thể cài đặt các phụ thuộc bằng cách sử dụng pip:

```bash
pip install numpy scikit-learn pyvi matplotlib seaborn
```
## Tiền xử lý dữ liệu
Dữ liệu văn bản thô được xử lý qua các bước sau:

- Đọc dữ liệu: Dữ liệu được tải từ các tệp JSON chứa văn bản và nhãn của chúng.
- Làm sạch văn bản: Loại bỏ các từ dừng (stopwords) và thực hiện các bước xử lý văn bản khác như chuyển chữ thường, loại bỏ dấu câu.
- Biểu diễn văn bản: Sử dụng phương pháp TF-IDF để chuyển đổi văn bản thành các vector số.
- Giảm chiều dữ liệu: Áp dụng PCA để giảm số chiều của các vector TF-IDF, giúp giảm độ phức tạp và tăng hiệu quả huấn luyện mô hình.

## Mô hình
Mô hình phân loại sử dụng Naive Bayes, có thể sử dụng hai phiên bản khác nhau tùy theo tính chất của dữ liệu:

- Naive Bayes Gaussian (GaussianNB): Phù hợp với dữ liệu liên tục, chẳng hạn như phân phối xác suất của các từ trong văn bản.

## Chạy chương trình
 ``` bash
python main.py
```

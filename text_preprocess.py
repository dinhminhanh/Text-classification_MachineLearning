import os
import json
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import numpy as np

data_path = "json"  # Thư mục chứa các file JSON
stopword_path = "vietnamese-stopwords.txt"  # File chứa danh sách từ dừng
def preprocess(data_path, stopword_path, dims=4096):
    data = []
    target = []
    target_names = []

    # Duyệt qua từng file trong thư mục
    for file_name in os.listdir(data_path):
        if file_name.endswith(".json"):  # Chỉ xử lý file .json
            # Đường dẫn file
            file_path = os.path.join(data_path, file_name)
            # Lấy nhãn từ tên file (bỏ phần .json)
            category = os.path.splitext(file_name)[0]

            # Thêm category vào danh sách nhãn nếu chưa có
            if category not in target_names:
                target_names.append(category)

           

            # Đọc file JSON
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                for item in json_data:
                    content = item.get("content", "").strip()
                    if content.lower() == "none":  # Loại bỏ content = "None"
                        continue
                    # Ghép nội dung từ title và content
                    text = (item.get("title", "") + " " + item.get("content", "")).strip()
                    data.append(text)
                    # Thêm chỉ số của category vào target
                    target.append(target_names.index(category))
                    
    # Đọc danh sách từ dừng
    with open(stopword_path, encoding="utf-8") as f:
        stopwords = f.readlines()
    stopwords = [x.strip().replace(" ", "_") for x in stopwords]

    # Tách từ tiếng Việt
    data = [ViTokenizer.tokenize(sample) for sample in data]

    # Chuyển văn bản thành biểu diễn TF-IDF vector
    tfidf_vector = TfidfVectorizer(stop_words=stopwords)
    data_preprocessed = tfidf_vector.fit_transform(data)
    
    # Chuyển dữ liệu TF-IDF thành ma trận
    tfidf_mat = data_preprocessed.toarray()

    # Áp dụng PCA để giảm chiều dữ liệu
    pca = PCA(n_components=dims)
    x_reduced = pca.fit_transform(tfidf_mat)

    return x_reduced, np.array(target), target_names



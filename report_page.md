# 📘 Report Lab 0 - Hello NLP

## 🚀 Pipeline thực hiện
Trong bài lab này, tôi đã thực hiện pipeline gồm các bước:

- Tạo môi trường bằng **Anaconda (Python 3.10)**  
- Cài đặt thư viện từ `requirements_core.txt`  
- Cài đặt **PyTorch với CUDA 12.1** (GPU)  
- Chạy kiểm tra môi trường: `env_check.py`  
- Chạy chương trình chính: `hello_nlp.py`  
- Thực thi kiểm thử bằng `pytest` (≥ 5 tests)  

## ⚠️ Vấn đề gặp phải & cách xử lý
Trong quá trình thực hiện, tôi gặp lỗi liên quan đến **OpenMP**:

> `libiomp5md.dll already initialized`

Nguyên nhân là do xung đột thư viện trong môi trường **Anaconda**.  

Cách khắc phục:
    $env:KMP_DUPLICATE_LIB_OK="TRUE"

Sau khi thiết lập biến môi trường, chương trình chạy bình thường.

## ✅ Kết quả đạt được
- PyTorch nhận diện GPU thành công: `cuda: True`  
- Các file **logs** và **results** được sinh đầy đủ  
- Các test chạy thành công (≥ 5 tests)  

## 📂 Minh chứng repository
Repository đã đảm bảo đầy đủ các thành phần yêu cầu:

- `README.md`  
- `src/`  
- `tests/` (≥ 5)  
- `logs/`  
- `results/`  
- `report_page.md`  
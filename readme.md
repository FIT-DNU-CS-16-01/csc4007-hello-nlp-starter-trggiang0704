[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1kZuF48d)

# CSC4007 — Lab0: Setup & Hello NLP

## 📌 Giới thiệu
Đây là bài Lab 0 của học phần Xử lý Ngôn ngữ Tự nhiên (NLP), nhằm mục tiêu:
- Thiết lập môi trường làm việc với Anaconda
- Làm quen với pipeline NLP cơ bản
- Kiểm tra hệ thống bằng script và test

---

## ⚙️ 1. Setup môi trường

Mở **Anaconda Prompt / Terminal** và chạy:

```bash
conda create -n csc4007-nlp python=3.10 -y
conda activate csc4007-nlp
python -m pip install -U pip
pip install -r requirements_core.txt
```

### (Optional - RAG)
```bash
pip install -r requirements_rag.txt
```

---

## 🚀 2. Cách chạy chương trình (How to run)

Chạy lần lượt:

```bash
python src/env_check.py
python src/hello_nlp_random.py
pytest -q
```

Hoặc chạy nhanh:

```bash
python src/env_check.py && python src/hello_nlp_random.py && pytest -q
```

---

## 📥 3. Input / Output

### Input
- Dữ liệu được tạo ngẫu nhiên trong code (không cần file input bên ngoài)

### Output (bắt buộc phải có)

Sau khi chạy sẽ sinh các file:

```
logs/lab0_run.log
logs/lab0_hello_nlp.log
results/lab0_env.json
results/lab0_metrics.json
```

### Ví dụ nội dung output

**lab0_metrics.json**
```json
{
  "config": {
    "seed": 42
  },
  "metrics": {
    "accuracy": 0.5,
    "macro_f1": 0.5
  }
}
```

---

## 🔁 4. Reproducibility

- Seed mặc định: **42**
- Được thiết lập trong `src/hello_nlp_random.py`
- Chạy nhiều lần sẽ cho kết quả giống nhau (đã có test kiểm chứng)

---

## ⚠️ 5. Responsible Use

- Dữ liệu sử dụng là dữ liệu **random**, không chứa thông tin cá nhân (PII)
- Không dùng cho mục đích thực tế
- Kết quả chỉ nhằm kiểm tra pipeline hoạt động
- Có thể tồn tại bias do dữ liệu ngẫu nhiên

---

## 🧪 6. Tests

Thư mục `tests/` gồm ≥ 5 test, bao gồm:

- Anti-leakage (BF1)
- Robustness input (BF2)
- Reproducibility (BF3)

Chạy test:

```bash
pytest -q
```

---

## 📂 7. Cấu trúc thư mục

```
src/
tests/
logs/
results/
README.md
report_page.md
```

---

## 📌 8. Checklist nộp bài

Repo cần có:

- README.md
- src/
- tests/ (>=5)
- logs/
- results/
- report_page.md

---

## 🤖 9. CI (GitHub Actions)

Mỗi lần push code, hệ thống sẽ tự động:

1. Cài thư viện
2. Chạy:
   ```bash
   python src/env_check.py
   ```
3. Chạy:
   ```bash
   python src/hello_nlp_random.py
   ```
4. Chạy:
   ```bash
   pytest -q
   ```

### ✅ PASS khi:
- Không lỗi runtime
- Có đủ logs + results
- Test pass hết

### ❌ FAIL khi:
- Thiếu file
- Sai đường dẫn
- Code lỗi
- Test fail

### Xem log:
- Vào tab **Actions** trên GitHub
- Click workflow bị ❌ để xem lỗi

---

## 👨‍💻 Tác giả

- Sinh viên: Trần Trường Giang
- Môn: CSC4007 — NLP

# 🚲 Bike Sharing Dashboard

Proyek ini merupakan bagian dari submission **Belajar Analisis Data dengan Python** di Dicoding. Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan dataset *Bike Sharing* dan menyajikannya dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## 📌 Deskripsi Proyek

Analisis difokuskan untuk menjawab beberapa pertanyaan bisnis, yaitu:

1. **Bagaimana tren jumlah penyewaan sepeda setiap harinya dan per jam?**
2. **Apa pengaruh musim dan kondisi cuaca terhadap jumlah penyewaan sepeda?**

Dataset yang digunakan:
- `day.csv` dan `hour.csv`: dataset asli
- `day_clean.csv`: dataset hasil pembersihan (digunakan di dashboard)

---

## 📊 Insight Utama

- Penyewaan sepeda meningkat saat musim **gugur** dan **panas**, dan menurun saat musim dingin.
- Penggunaan sepeda memuncak pada pagi dan sore hari.
- Cuaca cerah dan mendung ringan mendorong peningkatan penyewaan, sementara cuaca buruk menurunkannya drastis.

---

## 🚀 Cara Menjalankan Dashboard

### 1. Setup Virtual Environment (venv)

#### a. Buat Virtual Environment
```bash
python -m venv venv
```

#### b. Aktifkan Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  source venv/bin/activate
  ```

#### c. Install Library yang Dibutuhkan
```bash
pip install -r requirements.txt
```

---

### 2. Jalankan Aplikasi Streamlit

```bash
streamlit run dashboard.py
```

---

## 📦 Daftar Library

Semua kebutuhan library telah disimpan dalam file `requirements.txt` agar mudah direproduksi di environment lain. Contoh isi:

```
pandas==2.1.4
matplotlib==3.8.0
seaborn==0.13.0
streamlit==1.30.0
```

Jika ingin membuat ulang file ini secara otomatis, kamu bisa gunakan:

```bash
pip freeze > requirements.txt
```

Atau secara lebih efisien untuk proyek:
```bash
pip install pipreqs
pipreqs .
```

---

## 👤 Author
**Ferdy Luqman**  
Submission untuk course Dicoding: *Belajar Analisis Data dengan Python*

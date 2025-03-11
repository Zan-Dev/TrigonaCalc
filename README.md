# Web App dengan Flask dan Python

Proyek ini adalah web app yang dibangun menggunakan **Flask**, sebuah microframework untuk Python.

## 🚀 Persiapan Lingkungan
Sebelum menjalankan proyek, pastikan Anda telah menginstal **Python** dan mengikuti langkah-langkah berikut.

### 1️⃣ **Instalasi Python**
Pastikan Python 3 telah terinstal di sistem Anda. Jika belum, unduh dan instal dari [Python.org](https://www.python.org/downloads/).

Cek versi Python dengan menjalankan:
```bash
python --version
```
atau jika menggunakan `python3`:
```bash
python3 --version
```

### 2️⃣ **Membuat Virtual Environment**
Gunakan virtual environment untuk mengelola dependensi:
```bash
python -m venv venv
```
Aktifkan virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ **Instalasi Dependensi**
Instal Flask :
```bash
pip install flask
```

## 🔥 Menjalankan Aplikasi
Setelah semua persiapan selesai, jalankan aplikasi Flask:
```
flask --app src/app --debug run
```

```
Secara default, aplikasi akan berjalan di **http://127.0.0.1:5000/**.

## 📁 Struktur Proyek
```
/project-folder
│──  /src
|  |──  /static
|  |    |──  styles.css
|  |──  /templates
|  |    |──  index.html
|  │──  app.py
└──  README.md
```

## 🛠 Teknologi yang Digunakan
- **Python 3.12.3**
- **Flask**
- **HTML, CSS** *(untuk tampilan UI)*

## 🤝 Kontribusi
Jika ingin berkontribusi, silakan buat **pull request** atau ajukan **issue**.

---
Selamat coding! 🚀

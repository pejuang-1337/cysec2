# 🔐 CYSEC Toolkit

Toolkit Cyber Security berbasis Python & Flask yang memiliki fitur:
- 🧠 OSINT (Open Source Intelligence)
- 🐞 Web Bug Scanner
- 🎭 Social Engineering Simulation
- 📍 Location Tracker berbasis nomor HP (simulasi)

- cysec_web/
├── app.py
├── requirements.txt
├── modules/
│   ├── osint.py
│   ├── webscan.py
│   ├── soceng.py
│   └── location_tracker.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css


---

## 🌐 Demo Online
Tersedia via Replit (gratis):  
👉 [https://replit.com/@pejuanh1337/CyberSecurityScanner) *(setelah deploy)*

---

## 📦 Fitur

| Fitur              | Deskripsi                                                                 |
|--------------------|--------------------------------------------------------------------------|
| OSINT              | Menganalisis target berbasis username                                    |
| Web Scan           | Mengecek HTTP Headers dan informasi awal potensi bug                     |
| Social Engineering | Simulasi manipulasi berbasis nama dan relasi target                     |
| Location Tracker   | Simulasi pelacakan lokasi dari nomor HP (butuh API eksternal untuk nyata)|

---

## 🚀 Deploy Lokal

```bash
git clone https://github.com/pejuang-1337/cysec1.git
cd cysec1
pip install -r requirements.txt
python app.py

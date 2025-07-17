# SnapBG API

SnapBG is an **AI-powered background remover API** built using FastAPI and Rembg.  
Easily remove image backgrounds with a single API call. Perfect for e-commerce, design, and media apps.

---

## 🚀 Features
✔ Remove background from images in seconds  
✔ REST API with FastAPI  
✔ Free & Paid plans (when published on RapidAPI)  

---

## 📂 Project Structure
      snapbg-api/
│
├── main.py            # FastAPI app
├── requirements.txt   # Dependencies
├── .gitignore
└── README.md

---

## ✅ Installation (Local Setup)
```bash
# Clone the repository
git clone https://github.com/Rjcoder1008/snapbg-api.git
cd snapbg-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
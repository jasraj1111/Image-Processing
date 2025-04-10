
# 🖼️ Image Processing Suite - Streamlit + OpenCV

This project is a web-based image processing suite built with **Streamlit** and **OpenCV**. It allows users to perform various image processing operations such as resizing, grayscale conversion, histogram plotting, contrast enhancement, thresholding, and slicing techniques.



## 📌 Features

- 📷 Load and display a predefined image (`pic_1.jpg`, `pic_2.jpg`)
- 🔍 Convert RGB to Grayscale
- 📏 Resize image with adjustable scale
- 📊 View grayscale histogram
- 🌈 Perform contrast stretching
- 🔘 Apply binary thresholding
- 🎯 Perform graylevel slicing
- 🧠 Explore individual bit planes (Bit Plane Slicing)
- Smoothning using a 3x3 Kernel



## 📂 Folder Structure
├── app.py                  # Main Streamlit app
├── script1.py              # Basic image operations (display, resize, grayscale)
├── script2.py              # Advanced image processing (histogram, thresholding, etc.)
├── pic_1.jpg               # Preloaded test image 1
├── pic_2.jpg               # Preloaded test image 2
├── requirements.txt        # Dependencies for the project
└── README.md               # This file


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/image-processing-suite.git
cd image-processing-suite
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`.

---

## 🛠 Technologies Used

- [Streamlit](https://streamlit.io/) – For building the interactive UI
- [OpenCV](https://opencv.org/) – For image processing operations
- [NumPy](https://numpy.org/) – For array manipulation
- [Pillow (PIL)](https://python-pillow.org/) – Optional for image compatibility

---

## 🖼️ Preview

<img src="https://github.com/yourusername/image-processing-suite/blob/main/preview.gif" alt="App Preview" width="800"/>

---


## 👨‍💻 Author

**Jasraj Shendge**  
[GitHub](https://github.com/jasrajshendge) • [LinkedIn](https://linkedin.com/in/jasrajshendge)


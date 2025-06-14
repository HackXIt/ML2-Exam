# 📚 ML2 Exam Preparation – Jupyter + Anki MCQ System

This repository is designed to help you **prepare for the ML2 exam** by combining two powerful study tools:

* **Jupyter Notebooks** for explanation and guided walkthrough of each lecture slide
* **Anki decks** for active recall through MCQs (Multiple-Choice Questions)

---

## ✅ What You Need

1. **[Anki](https://apps.ankiweb.net/)** — a free, open-source flashcard app

   * Download and install for **Windows**, **macOS**, or **Linux**

2. **Install the Anki Add-on for MCQs**

   * Add-on ID: **`1566095810`**
   * In Anki:

     ```
     Tools → Add-ons → Get Add-ons → Paste: 1566095810
     ```

3. **Jupyter Notebook Viewer**

   * Install [JupyterLab](https://jupyter.org/install) locally or view notebooks on GitHub or with [nbviewer](https://nbviewer.org)

---

## 📁 Repository Structure

The repository contains one folder per ML2 topic. Inside each folder:

* The **lecture slides PDF** for that topic
* A **Jupyter notebook** with annotated explanations
* (Optional) CSV files with raw MCQs for that topic

An additional central **Anki/** folder contains all pre-built `.apkg` decks and generation scripts.

```
.
├── 01 - Multiple Linear Regression
│   ├── 01_MultipleRegression.pdf
│   └── Multiple Linear Regression.ipynb
├── 02 - Polynomial Regression - Splines
│   ├── 02_Polynomial-Spline-Regression-.pdf
│   └── Regression_Multi-Linear, Polynomial, and Splines.ipynb
├── 03 - Regularization Methods for Regression
│   ├── 03_RidgeLassoRegression.pdf
│   └── Regularization Methods for Regression.ipynb
├── 04 - ...
├── Anki
│   ├── ML2__Multi-Linear,Polynomial and Splines.apkg
│   └── ML2__Multiple Linear Regression.apkg
└── README.md
```

---

## 💡 Features

* Fully interactive **single- and multiple-answer MCQs**
* Automatic shuffling of answer options (via Add-on 1566095810)
* \[Correct] / \[Wrong] feedback with explanations
* Detailed Jupyter-based walkthroughs of each ML2 topic
* CSV-to-Anki conversion utilities included

---

## 🚀 How to Study

1. Open the **Jupyter notebook** for the topic and study the annotated slides
2. Open Anki and import the corresponding `.apkg` file from the `Anki/` folder:

   ```
   Anki → File → Import → Select .apkg file
   ```
3. Practice answering questions with randomized options and explanations
4. Repeat across all topics in the ML2 course

---

Prepare well — and good luck on the ML2 exam! 🎯📈

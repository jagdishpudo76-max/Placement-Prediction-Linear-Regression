# Placement Prediction Using Linear Regression

## 📌 Project Overview
This project focuses on predicting student placement packages based on their CGPA using **Simple Linear Regression**, a supervised machine learning algorithm.

The project uses historical placement data to understand the relationship between students' CGPA and their salary packages. A Linear Regression model is trained to predict the expected package based on CGPA.

## 🎯 Objectives
- Analyze student placement data.
- Understand the relationship between CGPA and package.
- Visualize placement data using scatter plots.
- Train a Linear Regression model.
- Predict student placement packages based on CGPA.

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook / Python IDE

## 📂 Project Structure

```text
Placement-Prediction/
│
├── placement.csv
├── placement_prediction.py
└── README.md
```

## 📊 Dataset Information

The dataset is stored in `placement.csv`.

It contains student placement information, including:

- **CGPA:** Student's academic performance.
- **Package:** Salary package offered to the student.

## ⚙️ Project Workflow

1. Import required Python libraries.
2. Load the placement dataset using Pandas.
3. Separate independent (CGPA) and dependent (Package) variables.
4. Explore the dataset using `head()` and `info()`.
5. Visualize CGPA vs Package using a scatter plot.
6. Split the dataset into training and testing sets.
7. Create a Linear Regression model.
8. Train the model using training data.
9. Predict placement packages using testing data.

## 🧠 Machine Learning Algorithm

**Simple Linear Regression**

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value based on input features.

The mathematical equation is:

Y = mX + C

Where:
- Y = Predicted Package
- X = Student CGPA
- m = Slope (Coefficient)
- C = Intercept

## 💻 Installation

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder.

3. Make sure `placement.csv` is available in the project directory.

4. Run the Python file:

```bash
python placement_prediction.py
```

## 📈 Data Visualization

A scatter plot is created to visualize the relationship between CGPA and placement packages.

- X-axis: CGPA
- Y-axis: Package

## 🔮 Prediction

The Linear Regression model predicts placement packages using the testing dataset.

The model uses:

- 80% data for training.
- 20% data for testing.
- Random State: 2.

## 🚀 Future Improvements

- Evaluate model performance using R² Score, MAE, and MSE.
- Add more student features such as skills and academic scores.
- Improve prediction accuracy.
- Build an interactive placement prediction web application using Flask or Streamlit.

## 👨‍💻 Author

**Jagdeesh Pudo**

GitHub: https://github.com/jagdishpudo76-max

LinkedIn: https://www.linkedin.com/in/jagdish-pudo-8b7193261/

## 📄 License

This project is created for educational and learning purposes.
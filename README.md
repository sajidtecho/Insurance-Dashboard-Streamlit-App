# 🏥Insurance-Dashboard-Streamlit-App
📊 Overview

Insurance Dashboard is an interactive data analytics and prediction app built using Streamlit.
It explores health insurance data to uncover patterns in medical charges and allows users to predict their future insurance cost with a customizable interest rate for upcoming years.

🚀 Features

✅ Cleaned and visualized the insurance.csv dataset
✅ Interactive dashboards for exploring:

Distribution of age, BMI, children, and charges

Impact of smoking status, gender, and region on insurance costs

Correlation between BMI, smoker habits, and medical charges

✅ Predictive feature:

Users can input their age, BMI, children, smoker status, etc.

The app predicts insurance cost using a trained ML model

Users can project the future insurance amount after adding an interest rate

🧠 Tech Stack

Python

Streamlit

Pandas / NumPy

Matplotlib / Seaborn

Scikit-learn

⚙️ Installation & Usage

Clone the repository:

git clone https://github.com/<your-username>/insurance-dashboard.git
cd insurance-dashboard


Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run insurance_dashboard.py


Open in your browser:
👉 http://localhost:8501

📈 Example Visuals

Correlation heatmap of numerical variables

Boxplots showing effect of smoking and region on charges

Prediction chart for future insurance cost

🤖 Future Improvements

Add authentication for users

Deploy app online (Streamlit Cloud / Render / HuggingFace Spaces)

Add API integration for real-time insurance updates

👨‍💻 Author

Sajid Ahmad
💼 Data Science & Machine Learning Enthusiast
🌐 LinkedIn Profile
 (add your real link)

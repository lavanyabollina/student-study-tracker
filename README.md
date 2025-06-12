# 📚 Student Study Tracker
A smart, responsive web app that helps students plan their study time effectively based on subject difficulty, familiarity, and priority using HTML, CSS, JavaScript, and Python (Flask). It leverages Linear Regression to generate personalized study schedules.

---
## ✅ Features

- ✅ Dynamic 3-step planner interface  
- ✅ Linear Regression-based study hour prediction  
- ✅ Responsive and animated UI with floating particles  
- ✅ Auto-distribution of subjects based on time availability  


---
## 📁 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript  
- **Backend:** Flask (Python)  
- **Machine Learning:** scikit-learn (Linear Regression)  
- **Libraries:** pandas  

---
## 🖥 How It Works

- ✍️ **User enters subjects and topics**
- 📊 **Inputs difficulty, familiarity & priority**
- ⏰ **Sets daily available hours and days till exam**
- 🤖 **Backend uses linear regression to suggest hours per subject**
- 📅 **Displays a generated daily study schedule in a clean table format**

---
# 🔧 Setup Instructions
1.Clone the repository
git clone https://github.com/lavanyabollina/student-study-tracker.git
cd student-study-tracker


2.Create a virtual environment (optional but recommended)  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3.Run the app
python app.py

---
## 📁 Folder Structure

student-study-tracker/
│
├── templates/
│ └── index.html
│
├── app.py
└── README.md

---
# 📈 ML Model Used
The project uses a **Linear Regression** model from the **scikit-learn** library to predict the suggested number of study hours based on:

- 📘 **Difficulty** (rated on a scale of 1 to 3)  
- 🧠 **Familiarity** (rated on a scale of 1 to 3)

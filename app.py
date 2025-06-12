from flask import Flask, request, render_template, jsonify
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)

# Sample training data (for predicting suggested study hours)
data = {
    "Difficulty": [2, 3, 5, 4, 3],
    "Familiarity": [5, 3, 2, 4, 3],
    "Suggested Hours": [4, 3.5, 2, 3.5, 3],
}
df = pd.DataFrame(data)

# Train a Linear Regression Model
X = df[["Difficulty", "Familiarity"]]
y = df["Suggested Hours"]
model = LinearRegression()
model.fit(X, y)

# Function to create the schedule with subjects spread across days
def create_schedule(subjects, difficulties, familiarity, priorities, time_per_day, total_days, topics, predicted_hours):
    weights = [(priority / difficulty) for priority, difficulty in zip(priorities, difficulties)]
    total_weight = sum(weights)
    total_hours = time_per_day * total_days
    allocated_hours = [(weight / total_weight) * total_hours for weight in weights]

    # Adjust allocated hours based on predicted hours
    allocated_hours = [min(allocated, predicted) for allocated, predicted in zip(allocated_hours, predicted_hours)]

    schedule = []
    day = 1
    subject_index = 0
    hours_remaining = allocated_hours[subject_index]

    while day <= total_days:
        if hours_remaining > time_per_day:
            schedule.append({
                "Day": day,
                "Subject": subjects[subject_index],
                "Topic": topics[subject_index][0],  # Use the first topic for simplicity
                "Difficulty": difficulties[subject_index],
                "Familiarity": familiarity[subject_index],
                "Priority": priorities[subject_index],
                "Hours": time_per_day
            })
            hours_remaining -= time_per_day
        else:
            schedule.append({
                "Day": day,
                "Subject": subjects[subject_index],
                "Topic": topics[subject_index][0],  # Use the first topic for simplicity
                "Difficulty": difficulties[subject_index],
                "Familiarity": familiarity[subject_index],
                "Priority": priorities[subject_index],
                "Hours": hours_remaining
            })
            subject_index += 1
            if subject_index < len(subjects):
                hours_remaining = allocated_hours[subject_index]
            else:
                break  # No more subjects to allocate
        day += 1

    return schedule

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_schedule", methods=["POST"])
def generate_schedule():
    try:
        input_data = request.json
        subjects = input_data["subjects"]
        difficulties = input_data["difficulties"]
        familiarity = input_data["familiarity"]
        priorities = input_data["priorities"]
        time_per_day = input_data["time_per_day"]
        total_days = input_data["total_days"]
        topics = input_data["topics"]

        # Ensure all values are numeric
        difficulties = [int(d) for d in difficulties]
        familiarity = [int(f) for f in familiarity]
        priorities = [int(p) for p in priorities]

        # Predict suggested study hours based on difficulty and familiarity
        predicted_hours = []
        for d, f in zip(difficulties, familiarity):
            predicted_hours.append(model.predict([[d, f]])[0])

        # Generate the study schedule
        schedule = create_schedule(subjects, difficulties, familiarity, priorities, time_per_day, total_days, topics, predicted_hours)

        return jsonify({"status": "success", "schedule": schedule, "predicted_hours": predicted_hours})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__== "__main__":
    app.run(debug=True)
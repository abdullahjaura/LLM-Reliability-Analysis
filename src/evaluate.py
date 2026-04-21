import pandas as pd
import random
import os

# Fake model (no API needed)
def fake_model_answer(question):
    possible_answers = [
        "Paris",
        "William Shakespeare",
        "Jupiter",
        "100",
        "Incorrect Answer"
    ]
    return random.choice(possible_answers)

# Load dataset
df = pd.read_csv("data/questions.csv")

results = []

for _, row in df.iterrows():
    question = row["question"]
    true_answer = str(row["answer"]).strip()

    model_answer = fake_model_answer(question)

    correct = true_answer.lower() in model_answer.lower()

    results.append({
        "question": question,
        "true_answer": true_answer,
        "model_answer": model_answer,
        "correct": correct
    })

# Save results
os.makedirs("results", exist_ok=True)
results_df = pd.DataFrame(results)
results_df.to_csv("results/results.csv", index=False)

# Print accuracy
accuracy = results_df["correct"].mean()
print(f"Accuracy: {accuracy * 100:.2f}%")
print(results_df)

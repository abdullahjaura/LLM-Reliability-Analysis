import pandas as pd
import os

# Simulated QA system outputs for demonstration
def baseline_model_answer(question: str) -> str:
    knowledge_base = {
        "What is the capital of France?": "Paris",
        "What is the capital of Japan?": "Tokyo",
        "What is the capital of Italy?": "Milan",
        "What is the capital of Canada?": "Toronto",
        "What is the capital of Brazil?": "Brasilia",
        "What is the largest planet?": "Jupiter",
        "What gas do plants absorb from the atmosphere?": "Oxygen",
        "What is the chemical symbol for gold?": "Au",
        "What is the boiling point of water in Celsius?": "100 degrees Celsius",
        "What force keeps planets in orbit around the sun?": "Gravity",
        "What is the hardest natural substance?": "Diamond",
        "How many bones are in the adult human body?": "206",
        "What organ pumps blood through the body?": "The heart",
        "What is H2O commonly called?": "Water",
        "What part of the plant conducts photosynthesis?": "Leaves",
        "Who wrote Hamlet?": "William Shakespeare",
        "What year did World War II end?": "1945",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "Who was the first President of the United States?": "George Washington",
        "In which country were the pyramids of Giza built?": "Egypt",
        "What wall fell in 1989 in Germany?": "Berlin Wall",
        "Who discovered penicillin?": "Louis Pasteur",
        "What ship famously sank in 1912?": "Titanic",
        "Who was known as the Maid of Orleans?": "Joan of Arc",
        "Which ancient civilization built Machu Picchu?": "The Incas",
        "What is 15 * 3?": "45",
        "What is 12 squared?": "144",
        "What is 100 divided by 4?": "25",
        "What is 9 + 17?": "26",
        "What is the square root of 81?": "9",
    }
    return knowledge_base.get(question, "I am not sure.")

def normalize(text: str) -> str:
    return str(text).strip().lower()

def classify_answer(true_answer: str, model_answer: str) -> str:
    true_norm = normalize(true_answer)
    pred_norm = normalize(model_answer)

    if true_norm == pred_norm:
        return "correct"

    if true_norm in pred_norm or pred_norm in true_norm:
        return "partial"

    synonym_pairs = [
        ("heart", "the heart"),
        ("leaf", "leaves"),
        ("inca", "the incas"),
        ("100", "100 degrees celsius"),
    ]

    for a, b in synonym_pairs:
        if (true_norm == a and pred_norm == b) or (true_norm == b and pred_norm == a):
            return "partial"

    return "incorrect"

df = pd.read_csv("data/questions.csv")
results = []

for _, row in df.iterrows():
    question = row["question"]
    true_answer = row["answer"]
    category = row["category"]

    model_answer = baseline_model_answer(question)
    error_type = classify_answer(true_answer, model_answer)
    correct_flag = error_type == "correct"

    results.append({
        "question": question,
        "true_answer": true_answer,
        "model_answer": model_answer,
        "category": category,
        "error_type": error_type,
        "correct": correct_flag
    })

results_df = pd.DataFrame(results)
os.makedirs("results", exist_ok=True)
results_df.to_csv("results/results.csv", index=False)

accuracy = results_df["correct"].mean()
error_counts = results_df["error_type"].value_counts()
category_accuracy = results_df.groupby("category")["correct"].mean().reset_index()

print(f"Overall Accuracy: {accuracy * 100:.2f}%")
print("\nError Type Counts:")
print(error_counts)
print("\nAccuracy by Category:")
print(category_accuracy)
print("\nSample Results:")
print(results_df.head(10))

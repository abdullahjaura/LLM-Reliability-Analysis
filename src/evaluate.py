import os
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

df = pd.read_csv("data/questions.csv")
results = []

for _, row in df.iterrows():
    question = row["question"]
    true_answer = str(row["answer"]).strip()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer the question briefly and directly."},
                {"role": "user", "content": question},
            ],
            temperature=0
        )

        model_answer = response.choices[0].message.content.strip()
        correct = true_answer.lower() in model_answer.lower()

        results.append({
            "question": question,
            "true_answer": true_answer,
            "model_answer": model_answer,
            "correct": correct
        })

    except Exception as e:
        results.append({
            "question": question,
            "true_answer": true_answer,
            "model_answer": f"ERROR: {e}",
            "correct": False
        })

results_df = pd.DataFrame(results)
os.makedirs("results", exist_ok=True)
results_df.to_csv("results/results.csv", index=False)

accuracy = results_df["correct"].mean()
print(f"Accuracy: {accuracy * 100:.2f}%")
print(results_df[["question", "model_answer", "correct"]])

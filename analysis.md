# LLM Reliability Evaluation – Mini Study

## 1. Objective

The goal of this project is to design a lightweight evaluation pipeline for assessing the reliability of short-answer QA systems. The focus is not just on overall accuracy, but on understanding *how* and *why* errors occur.

---


## 2. Methodology

### Dataset

* 30 curated factual questions
* Categories:

  * Geography
  * Science
  * History
  * Math

### Evaluation Approach

For each question:

* Generate responses using a rule-based baseline QA system to simulate varying levels of correctness
* Compare response to ground truth answer
* Classify result into:

  * **Correct** (exact match)
  * **Partial** (contains correct information but not exact)
  * **Incorrect** (wrong or unrelated)

### Metrics

* Overall accuracy
* Error type distribution
* Accuracy by category

---


## 3. Results

* **Overall Accuracy:** 73.33%
* **Error Breakdown:**

  * Correct: 22
  * Partial: 4
  * Incorrect: 4

### Accuracy by Category

* Math: 100%
* History: 80%
* Geography: 60%
* Science: 60%

---


## 4. Key Findings

### Deterministic vs Factual Tasks

The system performed significantly better on deterministic problems (math) than on factual recall tasks. This suggests that structured or rule-based reasoning is more reliable than knowledge retrieval.

### Partial Correctness is Common

Several responses contained partially correct information (e.g., correct concept but wrong detail). This highlights a limitation of strict exact-match evaluation.

### Category-Level Variability

Performance varied meaningfully across categories, indicating that evaluation should not rely solely on aggregate accuracy.

---


## 5. Limitations

* Uses a simulated baseline instead of a real LLM
* Small, manually curated dataset
* Heuristic-based classification (limited semantic understanding)
* Exact-match evaluation may undercount useful responses

---


## 6. Future Work

* Evaluate real LLM outputs (e.g., GPT, Claude)
* Expand dataset size and diversity
* Incorporate semantic similarity scoring (embedding-based evaluation)
* Improve error classification with more granular categories
* Compare multiple model baselines

---


## 7. Conclusion

This project demonstrates that evaluating model reliability requires more than measuring accuracy. Structured error classification and category-level analysis provide deeper insight into model behavior and failure modes.


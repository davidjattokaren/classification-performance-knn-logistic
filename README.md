# classification-performance-knn-logistic
Classification Performance Measurement / Evaluation for kNN &amp; Logistic Regression

## High Level Outline
- Brief background section: What is the problem?  Why is it important?  Who are the key stakeholders?
- Data Section
- Classification Modeling:
  - kNN
    - find the best "k" value to move forward with - loop through a list of odd numbers, e.g. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] and choose the "k" that produces the most accurate model
    - Train the final kNN model using the "k" from the step above.  
    - Create a table of performance measures that vary over a range of possible probability thresholds.  Each row will correspond to a probability threshold.  Columns should include the following: TN, TP, FN, FP, Precision, Recall, F1, and Accuracy
  - Logistic Model
    - Train a Logistic model
    - Create a table of performance measures as described above - but for the Logistic Model
  - Pick a "winning" model
    - Based on the various performance measures, decide which of the two modeling frameworks (kNN or Logistic) to move forward with.
- Careful evaluation of winning model performance measures: Using the previously created table of performance measures do the following...
  - Pick a relatively low probability threshold (in the range of 0 to 0.4) and then discuss the potential business ramifications of the corresponding performance measures.  Specific questions to try and answer...
    - How many False Positives?  What do these numbers represent?  What are the potential costs to the business if we were to make these mistakes in practice?
    - How many False Negatives?  What do these numbers represent?  What are the potential costs to the business if we were to make these mistakes in practice?
    - Which prediction mistakes do you consider to be more costly?
  - Choose 2 more probability thresholds and repeat the evaluation steps above.
  - Based on careful consideration of probability threshold options and the corresponding speculated risks/costs - which probability threshold should we go forward with?

## Part 1
Complete the outlined steps above using the SystemAdministrators.csv dataset.

Target Variable: task_completed

We have the task of helping the HR department with resource allocation across the business.  The hope is that if we can use machine learning to successfully predict task completions (as well when tasks are likely to NOT be completed) then HR can make better decisions about team assignments.

## Part 2
Complete the outlined steps above using the FlightDelays_Clean.csv dataset.

Target Variable: status_delayed

For the airline industry - the goal is to optimize the tuning of a classification model that predicts flights that are likely to be delayed.  We must think carefully about decisions that might be made in response to various predictions as well as the potential costs of those decisions.

## Part 3
Complete the outlined steps above using the loan_approval.csv dataset.

Target Variable: approved

For a large regional bank - Your task is to create a prediction model that could be used to automate loan approval decisions.  There are some fields in this dataset that we WOULD NOT be allowed to use in practice (at least not in the U.S. or Europe).  We must think about the ethical issues surrounding the possibility of using variables like ethnicity, age, etc. when deciding to approve or reject a loan application.

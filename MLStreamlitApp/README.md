# ML Classification Explorer

**Deployed app:** [https://macher-ml-explorer.streamlit.app](https://macher-ml-explorer.streamlit.app)

## Overview

For this project I took the classification stuff we did in class (logistic regression, decision trees, random forests, and KNN) and made it into a Streamlit app. In the notebooks we had to change the code every time we wanted to try a different setting, so the idea here is that you can change everything with sliders and dropdowns and the results update right away.

Here's what you can do in the app:

- Upload your own CSV, or use the sample dataset I included (Greece Travel Data from Kaggle)
- Pick the target column you want to predict and which value counts as the "positive" class (1). For the sample data it starts on Mode of Travel = Flight, but you can change it.
- Pick which columns to use as features
- Choose a model and adjust its hyperparameters
- Change the test size for the train/test split
- See accuracy, precision, recall, F1, and ROC AUC on the test set, with a short explanation of what each one means
- See a confusion matrix and ROC curve, plus a feature importance chart for the tree models

## How to Run It Locally

1. Clone the repo and go into the app folder:
   ```bash
   git clone https://github.com/hmacher27/MACHER-Data-Science-Portfolio.git
   cd MACHER-Data-Science-Portfolio/MLStreamlitApp
   ```
2. (Optional) Make a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```
3. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
5. It should open in your browser at `http://localhost:8501`. The sample data is already in the `greece_data` folder so you don't need to download anything.

## Libraries

These are the versions in `requirements.txt`:

- streamlit 1.62.0
- pandas 3.1.1
- scikit-learn 1.9.1
- matplotlib 3.11.2
- seaborn 0.13.2

## Models and Hyperparameters

All the hyperparameters are in the sidebar. Every time you change one, Streamlit reruns the script, so the model retrains and the metrics and charts update.

- **Logistic Regression:** `C` (regularization). A smaller C means more regularization, so the model is simpler and less likely to overfit.
- **Decision Tree:** `max_depth`, `min_samples_split`, and `criterion`. `max_depth` is how many levels the tree can have. Deeper trees fit the training data better but can overfit. `min_samples_split` is how many rows a node needs before it can split. `criterion` is either gini or entropy, which is how the tree decides what a good split is.
- **Random Forest:** `n_estimators` and `max_depth`. `n_estimators` is how many trees are in the forest (each one is trained on a bootstrap sample and they vote). `max_depth` limits how deep each tree goes.
- **K-Nearest Neighbors:** `n_neighbors` (k). This is how many of the closest points vote on the prediction. A small k can overfit and a big k can underfit.

## Preprocessing

- Rows with missing values in the selected columns get dropped
- The target gets turned into 0/1 (1 = the positive class you pick), like how we made a binary target in class
- Text columns get one-hot encoded with `pd.get_dummies(drop_first=True)`
- Only columns with 20 or fewer unique values show up as target options, since this is classification
- The app checks that both classes have at least 10 rows before training so it doesn't crash
- For logistic regression and KNN, I scale the features with `StandardScaler`. I fit the scaler on the training data only so the test data doesn't leak in.

## About the Sample Data

The Greece Travel Data (3,000 trips) is synthetic, meaning it was generated and the columns aren't really related to each other. So the models don't do much better than guessing on it (ROC AUC around 0.5) no matter what you change. I left it in because it shows how all the app's features work. If you upload a real dataset, the models can actually find patterns.

## References

- [Streamlit documentation](https://docs.streamlit.io/): used for the widgets, layout, and deploying on Community Cloud
- [scikit-learn supervised learning guide](https://scikit-learn.org/stable/supervised_learning.html): used for the models and their hyperparameters
- [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html): used for the metrics
- [Greece Travel Data on Kaggle](https://www.kaggle.com/datasets/teamincribo/greece-travel-data): the sample dataset

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score

st.set_page_config(page_title="ML Explorer", layout="wide")

st.title("Machine Learning Explorer")
st.write("Upload a dataset (or use the Greece travel sample), pick a target, train a model, and see how it does!")

# load the data
st.sidebar.header("1. Data")
data_choice = st.sidebar.radio("Choose a dataset", ["Greece Travel Data (sample)", "Upload my own CSV"])

if data_choice == "Upload my own CSV":
    uploaded_file = st.sidebar.file_uploader("Upload a CSV", type="csv")
    if uploaded_file is None:
        st.info("Upload a CSV file to get started.")
        st.stop()
    df = pd.read_csv(uploaded_file)
else:
    # Greece Travel Data 
    path = os.path.join(os.path.dirname(__file__), "greece_data", "travel_tourism_dataset.csv")
    df = pd.read_csv(path)

st.header("The Data")
st.write("Shape:", df.shape)
st.dataframe(df.head())

# pick the target and features
st.sidebar.header("2. Target and Features")
columns = list(df.columns)
target_options = [c for c in columns if df[c].nunique() <= 20]
if len(target_options) == 0:
    st.warning("None of the columns look like categories (20 or fewer unique values), so there's nothing to predict. Try a different CSV.")
    st.stop()
default_target = target_options.index("Mode of Travel") if "Mode of Travel" in target_options else 0
target = st.sidebar.selectbox("Target column", target_options, index=default_target)

# make the target binary 
target_values = list(df[target].dropna().astype(str).unique())
default_positive = target_values.index("Flight") if "Flight" in target_values else 0
positive_class = st.sidebar.selectbox("Positive class (1)", target_values, index=default_positive)

feature_options = [c for c in columns if c != target]
default_features = [c for c in ["Duration", "Cost of Travel(Entire Trip)", "Stay", "Age", "Sex"] if c in feature_options]
features = st.sidebar.multiselect("Features", feature_options, default=default_features)
if len(features) == 0:
    st.warning("Pick at least one feature.")
    st.stop()

# drop missing values 
df_clean = df[features + [target]].dropna()
X = pd.get_dummies(df_clean[features], drop_first=True)  # drop_first avoids the dummy trap
y = (df_clean[target].astype(str) == positive_class).astype(int)

# make sure both classes have enough rows
if y.value_counts().min() < 10 or y.nunique() < 2:
    st.warning("Not enough rows in one of the classes. Try a different target or positive class.")
    st.stop()

# train/test split
st.sidebar.header("3. Train/Test Split")
test_size = st.sidebar.slider("Test size", 0.1, 0.5, 0.2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# pick a model and its hyperparameters
st.sidebar.header("4. Model")
model_name = st.sidebar.selectbox("Model", ["Logistic Regression", "Decision Tree", "Random Forest", "KNN"])

if model_name == "Logistic Regression":
    C = st.sidebar.select_slider("C (regularization)", [0.01, 0.1, 1.0, 10.0, 100.0], value=1.0)
    model = LogisticRegression(C=C, max_iter=1000)
elif model_name == "Decision Tree":
    max_depth = st.sidebar.slider("max_depth", 1, 20, 4)
    min_samples_split = st.sidebar.slider("min_samples_split", 2, 20, 2)
    criterion = st.sidebar.selectbox("criterion", ["gini", "entropy"])
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split,
                                   criterion=criterion, random_state=42)
elif model_name == "Random Forest":
    n_estimators = st.sidebar.slider("n_estimators", 10, 300, 100, step=10)
    max_depth = st.sidebar.slider("max_depth", 1, 20, 10)
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
else:
    k = st.sidebar.slider("n_neighbors (k)", 1, 25, 5, step=2)
    model = KNeighborsClassifier(n_neighbors=k)

# scale the features for logistic regression and KNN 
if model_name in ["Logistic Regression", "KNN"]:
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

# train the model 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_probs = model.predict_proba(X_test)[:, 1]

# evaluate the model
st.header(f"Results: {model_name}")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Accuracy", round(accuracy_score(y_test, y_pred), 2))
col2.metric("Precision", round(precision_score(y_test, y_pred, zero_division=0), 2))
col3.metric("Recall", round(recall_score(y_test, y_pred, zero_division=0), 2))
col4.metric("F1 Score", round(f1_score(y_test, y_pred, zero_division=0), 2))
col5.metric("ROC AUC", round(roc_auc_score(y_test, y_probs), 2))

st.markdown(f"""
**What do these mean?**
- **Accuracy:** the percent of test rows the model got right. Can be misleading if one class is way more common.
- **Precision:** when the model predicts '{positive_class}', how often it's actually right (few false alarms).
- **Recall:** out of all the real '{positive_class}' rows, how many the model caught (few misses).
- **F1 Score:** a balance of precision and recall. It's only high if both are high.
- **ROC AUC:** how well the model separates the two classes. 0.5 = random guessing, 1.0 = perfect.
""")

# confusion matrix and ROC curve (same as the in-class notebooks)
left, right = st.columns(2)
with left:
    st.subheader("Confusion Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    st.pyplot(fig)
    st.caption("The diagonal shows correct predictions. Off-diagonal boxes are mistakes.")
with right:
    st.subheader("ROC Curve")
    fpr, tpr, thresholds = roc_curve(y_test, y_probs)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, lw=2, label=f'ROC Curve (AUC = {roc_auc_score(y_test, y_probs):.2f})')
    ax.plot([0, 1], [0, 1], lw=2, linestyle='--', label='Random Guess')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.legend(loc="lower right")
    st.pyplot(fig)
    st.caption("The closer the curve gets to the top-left corner, the better the model.")

if model_name in ["Decision Tree", "Random Forest"]:
    st.subheader("Feature Importance")
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x=importances.values, y=importances.index, ax=ax)
    ax.set_xlabel('Importance')
    st.pyplot(fig)

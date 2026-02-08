import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache data loading
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load data
df, target_names = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# App Title
st.title("🌸 Iris Flower Prediction App")

st.subheader("Input Features")

# Sliders
sepal_length = st.slider(
    "Sepal Length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.slider(
    "Sepal Width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.slider(
    "Petal Length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.slider(
    "Petal Width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# Create input dataframe
input_data = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=df.columns[:-1]
)

# Prediction
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

# Output
st.subheader("Prediction Result")
st.success(f"Predicted Species: {target_names[prediction[0]]}")

st.subheader("Prediction Probability")
st.write(prediction_proba)

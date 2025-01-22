
import streamlit as st
import pandas as pd

# Initialize session state
if 'students' not in st.session_state:
    st.session_state.students = []

st.title("Student Score Tracker")

# Input area for student name and score
st.subheader("Add New Student")
name = st.text_input("Student Name")
score = st.number_input("Score", min_value=0, max_value=100, step=1)

# Button to add student
if st.button("Add Student"):
    if name and score is not None:
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f"Added {name} with a score of {score}")

# Display student data
st.subheader("Student Data")
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)

    # Filter students based on minimum score
    min_score = st.slider("Filter by Minimum Score", 0, 100, 0)
    filtered_df = df[df["Score"] >= min_score]

    st.write(filtered_df)
else:
    st.write("No student data available yet.")
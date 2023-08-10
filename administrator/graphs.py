import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import mysql.connector
from mysql.connector import Error


# Settings
st.set_option("deprecation.showPyplotGlobalUse", False)
style = """
<style>
.ea3mdgi2{
display: none;
}
</style>
"""
st.markdown(style, unsafe_allow_html=True)


# Functions
def get_data(table):
    try:
        connection = mysql.connector.connect(
            host="localhost", database="student_feedback", user="root", password=""
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            # Example: Fetch all rows from a table
            cursor.execute(f"SELECT * FROM {table}")
            data = cursor.fetchall()

            cursor.close()

            return data

    # Execute SQL queries here

    except Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed")

    return []


def piechart(sizes, labels, title):
    plt.figure(figsize=[2, 2])
    # Create a pie chart
    plt.pie(
        sizes,
        # explode=explode,
        labels=labels,
        # colors=colors,
        autopct="%1.1f%%",
        # shadow=True,
        startangle=140,
        radius=float(0.5),
    )
    plt.axis("equal")  # Equal aspect ratio ensures the pie is circular

    # Add a title
    plt.title(title, fontsize="5")
    return plt.show()


def format_data(data):
    pass


txt = st.experimental_get_query_params()


if txt["page"][0] == "course":
    course_df = get_data("student_answers")
    st.title("Course Review")
    column = [
        "lecturer_preparedness",
        "lecturer_interest",
        "feedback_useful",
        "lecturers_complement",
        "instructional_materials",
        "course_organization",
        "confidence_in_advanced_work",
        "exam_measurement",
        "concept_understanding",
        "concept_understanding_feedback",
        "applicability",
        "applicability_reasoning",
        "recommend_course",
        "course_info",
    ]


elif txt["page"][0] == "facilities":
    course_df = get_data(
        "facilities",
    )
    st.title("Facilities Review")
    column = [
        "id" "halls_of_residence",
        "cafeterias",
        "Lecture_rooms",
        "sports_equipment",
        "facility_availability",
        "equipment_access",
        "usage_frequency",
        "Labs_usage",
        "facility_up_to_date",
        "school_resources_availability",
        "library_usage",
        "coursework_improvement",
        "sports_equipment_adequacy",
        "sports_facilities_wish",
        "equipment_wish",
        "experience_improvement",
        "overall_satisfaction",
        "info",
    ]


elif txt["page"][0] == "instructors":
    course_df = get_data("student_answers")
    st.title("Instructors Review")
    column = [
        "lecturer_preparedness",
        "lecturer_interest",
        "feedback_useful",
        "lecturers_complement",
        "instructional_materials",
        "course_organization",
        "confidence_in_advanced_work",
        "exam_measurement",
        "concept_understanding",
        "concept_understanding_feedback",
        "applicability",
        "applicability_reasoning",
        "recommend_course",
        "course_info",
    ]


df = pd.DataFrame(
    course_df,
    columns=column,
)

graph_choices = st.multiselect("Select the fields for the graph", df.columns)
graph = st.selectbox(
    "Which graph do you want to see?", ["Line Graph", "Bar Graph", "Pie Chart"]
)


if graph == "Line Graph":
    st.line_chart(df[graph_choices].dropna())
elif graph == "Bar Graph":
    st.bar_chart(df[graph_choices].dropna())
elif graph == "Pie Chart":
    pie_chart = st.selectbox("Select A column", df.columns)
    st.pyplot(
        piechart(
            dict(df[pie_chart].value_counts().items()).values(),
            dict(df[pie_chart].value_counts().items()).keys(),
            pie_chart,
        ),
    )

# num = st.slider("Number of rows", min_value=1, max_value=len(df))

table_choices = st.multiselect("Select the fields for the table", df.columns)

st.dataframe(df[table_choices].dropna(), width=600)

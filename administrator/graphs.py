import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
def get_data(url):
    # Set up credentials
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("token.json", scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet by title
    sheet = client.open_by_url(url)

    # Create spreadsheet
    # sheet = client.create("A new spreadsheet")

    # Select a specific worksheet by index (0 for the first worksheet)
    worksheet = sheet.get_worksheet(0)

    # Get all values from the worksheet
    data = worksheet.get_all_values()

    return data


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
    course_df = get_data(
        "https://docs.google.com/spreadsheets/d/1vJ_63644dy2kdii_0S2W3iof__S8u9wvZtHmcoTmt0Y/edit#gid=1317552499"
    )
    st.title("Course Review")
    types = {
        "How satisfied are you with the overall quality of the courses offered at the university?": int,
        "How would you rate the effectiveness of the teaching methods used in the courses?": int,
        "How well do the courses foster critical thinking, problem-solving, and analytical skills?": int,
    }

elif txt["page"][0] == "facilities":
    course_df = get_data(
        "https://docs.google.com/spreadsheets/d/1rHKhgOm4rDUPKsVxr874XCpYKt3OeRTFf2ri9evQx8w/edit?resourcekey#gid=1372655742"
    )
    st.title("Facilities Review")
    types = {
        "How would you rate the overall quality of the university's facilities? (Scale: Poor - Excellent)": int,
        "Based on your experience with the university's facilities, how likely are you to recommend the university to prospective students? (Scale: Not Likely - Very Likely)": int,
        "How satisfied are you with the laboratory facilities in your department? (Scale: Not Satisfied - Very Satisfied)": int,
        "How satisfied are you with the condition and technology available in classrooms and lecture halls? (Scale: Not Satisfied - Very Satisfied)": int,
    }

elif txt["page"][0] == "instructors":
    course_df = get_data(
        "https://docs.google.com/spreadsheets/d/1VFQySLxpe4TChvthQzx8cGG3F3Invaqfru6AMg4AjB8/edit?resourcekey#gid=1935663529"
    )
    st.title("Instructors Review")
    types = {
        "How satisfied are you with the overall teaching quality of this instructor? (Scale: Very Dissatisfied - Very Satisfied)": int,
        "How well did the instructor use a variety of teaching methods to engage students in the learning process? (Scale: Not Well - Very Well)": int,
        "How clear and understandable were the instructor's explanations of complex topics? (Scale: Not Clear - Very Clear)": int,
        "How accessible was the instructor outside of class for questions and clarifications? (Scale: Not Accessible - Very Accessible)": int,
        "Based on your experience with this instructor, how likely are you to enroll in another course taught by them? (Scale: Not Likely - Very Likely)": int,
    }


df = pd.DataFrame(course_df[1:], columns=course_df[0])


df = df.astype(types)
numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
numerical_df = df.select_dtypes(include=numerics)

graph_choices = st.multiselect("Select the fields for the graph", numerical_df.columns)
graph = st.selectbox(
    "Which graph do you want to see?", ["Line Graph", "Bar Graph", "Pie Chart"]
)


if graph == "Line Graph":
    st.line_chart(numerical_df[graph_choices].dropna())
elif graph == "Bar Graph":
    st.bar_chart(numerical_df[graph_choices].dropna())
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

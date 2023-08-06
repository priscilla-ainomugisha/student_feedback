import streamlit as st
import pandas as pd
import os

# st.experimental_set_query_params(query_params={"page": ""})
txt = st.experimental_get_query_params()
df = pd.read_csv("mine.csv")
# st.write(txt["page"][0])

# df = pd.DataFrame(response.data * num)
# df.drop("Token", axis=1)
if txt["page"][0] == "course":
    st.title("Course Review")
elif txt["page"][0] == "facilities":
    st.title("Facilities Review")
elif txt["page"][0] == "instructors":
    st.title("Instructors Review")

style = """
<style>
.ea3mdgi2{
display: none;
}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

graph_choices = st.multiselect("Select the fields for the graph", df.columns)
graph = st.selectbox("Which graph do you want to see?", ["Line Graph", "Bar Graph"])

if len(graph_choices) < 1:
    pass
elif graph == "Line Graph":
    st.line_chart(df[graph_choices].dropna())
elif graph == "Bar Graph":
    st.bar_chart(df[graph_choices].dropna())


num = st.slider("Number of rows", min_value=1, max_value=len(df))

table_choices = st.multiselect("Select the fields for the table", df.columns)

st.dataframe(df[table_choices][:num].dropna(), width=600)

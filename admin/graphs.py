import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")

# supabase: Client = create_client(url, key)

# response = supabase.table("course_review").select("*").execute()

df = pd.read_csv("mine.csv")

# df = pd.DataFrame(response.data * num)
# df.drop("Token", axis=1)

# st.write(response.data)

st.title("Course Review")
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

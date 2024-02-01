import streamlit

streamlit.title('Hi There! Krupa here')
streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗 Blueberries and Oats')
streamlit.text('Ramen Noodles and Sausages🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

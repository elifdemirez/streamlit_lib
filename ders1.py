import streamlit as st
import pandas as pd
tabel=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})
st.title("Hi I am Streamlit Web App")
st.subheader("Hi I am your subheader")
st.header("I am Header")
st.text("Hi I am text function and programmers uses")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("Hello world")
def func():
return 0;
def func()
"""
st.code(code,language="python")
st.write("## H2")
st.metric(label="Wind Speed",value="120ms⁻¹ ",delta="-1.4ms⁻¹ ")
st.table(tabel)
st.dataframe(tabel)
st.image("Image.jpg",caption="this is my Image",width=680)
st.audio("Audio.mp3")
# st.video()
def change():
    print(st.session_state.checker)
state=st.checkbox("Checkbox",value=True,on_change=change,key="checker")
radio_btn=st.radio("In which country do you live?",options=("US","UK","Canada"))
print(radio_btn)
def btn_click():
    print("Button Clicked")

btn=st.button("Click Me!", on_click=btn_click)
select=st.selectbox("What is your favourite car?",options=("Audi","BMW","Ferrari"))
print(select)
multi_select=st.multiselect("What is your favourite Tech Brand?",options=("Microsoft","Apple","Oracle"))
st.write(multi_select)
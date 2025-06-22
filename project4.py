import streamlit as st

st.set_page_config(page_title='Trắc nghiệm tính cách', page_icon=':question:', layout='wide')
st.title('Hãy chọn một con vật bạn yêu thích')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con sư tử')
with col4:
    b4 = st.button('Con ngựa')
with col5:
    b5 = st.button('Thiên nga')

with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    if b1:
        st.write('Con vật bạn chọn là con mèo')
    if b2:
        st.write('Con vật bạn chọn là con chó')
    if b3:
        st.write('Con vật bạn chọn là con sư tử')
    if b4:
        st.write('Con vật bạn chọn là con ngựa')
    if b5:
        st.write('Con vật bạn chọn là thiên nga')
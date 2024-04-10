

# Import Streamlit
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Front_Page",
    page_icon="person",
)
#st.markdown("""Check [Multi Disease Prediction system](https://publicmlwebapp-xtuzve6splj7hyxm6sl3nw.streamlit.app/) """)





# Main Page
st.markdown("<h1 style='text-align: center; color: WHITE; font-size:20;'>Poly-Patho-Prognosis</h1>", unsafe_allow_html=True)
#st.title("Poly-Patho-Prognosis")
#st.sidebar.success("Select a page above.")


# Projects Page

st.markdown('#')
st.markdown("<h3 style='text-align: left; color: WHITE; font-size:20;'>By :</h3>", unsafe_allow_html=True)
#st.title("By: ")
col1, col2 = st.columns(2)
with col1:
    st.write("Tanushree Dhali:12621001187")
with col2:
    st.write("tanushree.dhali.cse24@heritageit.edu.in")
with col1:
    st.write("Deboleena Ghosh:  12620003058")
with col2:
    st.write("deboleena.ghosh.cse24@heritageit.edu.in")

with col1:
    st.write("Prerana Saha:   12620001087")
with col2:
    st.write("prerana.saha.cse24@heritageit.edu.in")
with col1:
    st.write("Dipshikha Mondal: 12621001173")
with col2:
    st.write("dipshikha.mondal.cse24@heritageit.edu.in")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.vecteezy.com/system/resources/thumbnails/006/736/873/small_2x/abstract-blue-circuit-digital-background-free-vector.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
# Contact Page
st.title(" ")
st.write("\n")
st.markdown('##')
#url = 'https://publicmlwebapp-xtuzve6splj7hyxm6sl3nw.streamlit.app/'
#st.markdown(f'''
#<a href={url}><button style="display:block;margin:auto; color: blue; text-align: center;background-color:Gray;">Multi Disease Prediction system</button></a>
#''',
#unsafe_allow_html=True)



col1, col2, col3 = st.columns(3)

with col1:
    pass
with col3:
    pass
with col2:
    center_button = st.link_button("Prediction System", "https://poly-patho-prognosis-1.streamlit.app/",use_container_width=True)
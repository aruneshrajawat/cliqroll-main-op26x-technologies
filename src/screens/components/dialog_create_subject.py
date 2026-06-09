import streamlit as st
from src.screens.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter New Subject Details")
    sub_id = st.text_input("Subject Code", placeholder="CS101", key="dlg_sub_code")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science", key="dlg_sub_name")
    sub_section = st.text_input("Section", placeholder="A", key="dlg_sub_section")

    if st.button("Create Subject Now", key="dlg_create_btn"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, teacher_id, sub_section)
                st.session_state["subject_created"] = True
                st.rerun()
            except Exception as e:
                st.error(f"Error creating subject: {e}")
        else:
            st.warning("Please fill in all the details to create a subject.")

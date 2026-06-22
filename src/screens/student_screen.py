import streamlit as st
from src.screens.ui.base_layout import style_background_dashboard
from src.screens.components.header import header_dashboard
from src.screens.ui.base_layout import style_base_layout
from src.screens.components.footer import footer_dashboard
from src.screens.pipelines.face_pipeline import predict_attendance,get_face_embeddings,train_classifier
from src.screens.database.db import get_all_students,create_student,get_student_subjects,get_student_attendance
from src.screens.pipelines.voice_pipeline import get_voice_embeddings
from src.screens.components.dialog_enroll import enroll_dialog
from src.screens.database.db import unenroll_student_to_subject
from src.screens.components.subject_card import subject_card
import numpy as np
from PIL import Image

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1,c2 = st.columns(2,vertical_alignment="center",gap= "xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"welcome {student_data['name']}")

        if st.button("Logout",type = 'secondary',key = "loginbackbtn",shortcut = "control+spacebar"):
            st.session_state["is_logged_in"] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1,c2 = st.columns(2)
    with c1:
        st.header("Your Enrolled Student")
    with c2:
        if st.button("enroll in subject",type = 'primary',width = 'stretch'):
            enroll_dialog()


    st.divider()
    with st.spinner("Loading your enrolled subjects..."):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}
    
    for log in logs:
        sid = log["subject_id"]

        if sid not in stats_map:
            stats_map[sid]= {'total':0,"attended":0}

        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]["attended"] += 1
        
    cols = st.columns(2)
    for i ,sub_node in enumerate (subjects):
        sub = sub_node ['subjects']
        sid = sub["subject_id"]

        stats = stats_map.get(sid,{'total':0,"attended":0})
        def unenroll_btn():
            if st.button("Unenroll from this Course",type = 'secondary',width = 'stretch',icon = ":material/delete_forever:"):
                unenroll_student_to_subject(student_id,sid)
                st.toast(f"Unenrolled from {sub['name']} successfully!")
        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📆', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
            )
            if st.button("Unenroll", key=f"unenroll_{sid}_{i}", type='secondary', use_container_width=True):
                unenroll_student_to_subject(student_id, sid)
                st.rerun()


    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return 
    c1,c2 = st.columns(2,vertical_alignment="center",gap= "xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back To Home",type = 'secondary',key = "loginbackbtn",shortcut = "control+spacebar"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.markdown(
    '<h2 style="white-space: nowrap; font-size: 1.6rem;">Login using Face ID</h2>',
    unsafe_allow_html=True
    )

    st.space()

    show_registeration = False

    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner("Recognizing..."):
            detected , all_ids, num_faces, all_students_ids = predict_attendance(img)
            if num_faces == 0:
                st.error("No face detected. Please try again.")
            if num_faces>1:
                st.warning("Multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()

                    student = next((s for s in all_students if s['student_id']==student_id), None)
                    if student:
                        st.session_state.is_logged_in = True 
                        st.session_state.user_role= 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student["name"]}")
                        import time
                        time.sleep(1)
                        st.rerun()

                else:
                    st.info("Face not recognized. You might be a new Student! ")
                    show_registeration = True 
    
    if show_registeration:
        with st.container(border = True):
            st.header("It seems you are new here! Let's get you registered")
            new_name = st.text_input("Enter your name", placeholder = 'E.g Arunesh Singh Rajawat')
            st.subheader('optional:Voice Enrollment')
            st.info("Voice enrollment is optional but can help in improving the accuracy of attendance marking. You can enroll your voice by recording a short audio clip of yourself saying a specific phrase.")
            audio_data = None

            try:
                audio_data = st.audio_input("Record your short voice phrase for enrollment")
            except Exception as e:
                st.warning("Audio input is not supported in your browser. Voice enrollment will be skipped.")
            if st.button("Create Account",type = "primary"):
                if new_name:
                    with st.spinner("Creating profile... "):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb= encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embeddings(audio_data.read())
                            response_data = create_student(new_name,face_embedding = face_emb,voice_embedding = voice_emb)
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True 
                                st.session_state.user_role= 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile created ! Hi {new_name}")
                                import time
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.error("couldn't capture your facial feature for registration")
                    

        st.markdown(
        '<h2 style="white-space: nowrap; font-size: 1.6rem;text_alignment = "center";">Register using Face ID</h2>',
        unsafe_allow_html=True
        )
        if st.button("Register Now",type = 'primary',width = 'stretch'):
            st.session_state.student_photo = photo_source
            st.session_state.student_login_type = "register"
            st.rerun()
        
        
    footer_dashboard()


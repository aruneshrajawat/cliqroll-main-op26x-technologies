import streamlit as st
from src.screens.ui.base_layout import style_background_dashboard
from src.screens.components.header import header_dashboard
from src.screens.ui.base_layout import style_base_layout
from src.screens.components.footer import footer_dashboard
from src.screens.database.db import check_teacher_exists,check_teacher_email_exists,create_teacher,teacher_login,get_teacher_subjects
from src.screens.components.dialog_create_subject import create_subject_dialog
from src.screens.components.subject_card import subject_card
from src.screens.components.dialog_share_subject import  share_subject_dialog
from src.screens.components.dialog_add_photo import add_photo_dialog
from src.screens.pipelines.face_pipeline import predict_attendance
from PIL import Image
from src.screens.database.config import supabase
import numpy as np
from datetime import datetime
import pandas as pd
from src.screens.components.dialog_attendance_result import attendance_result_dialog
from src.screens.components.dialog_voice_attendance import voice_attendance_dialog
from src.screens.database.db import get_attendance_for_teacher
def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state. teacher_login_type =="login":
        teacher_screen_login()
    elif st.session_state. teacher_login_type == "register":
        teacher_screen_register()

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1,c2 = st.columns(2,vertical_alignment="center",gap= "xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"welcome {teacher_data['name']}")

        if st.button("Logout",type = 'secondary',key = "loginbackbtn",shortcut = "control+spacebar"):
            st.session_state["is_logged_in"] = False
            del st.session_state.teacher_data
            st.rerun()
    st.space()
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendance"
    tab1,tab2,tab3 = st.columns(3)
    with tab1:
        type1 = 'primary' if st.session_state.current_teacher_tab == 'take_attendance' else 'tertiary'
        if st.button("Take Attendance",type = type1,width = 'stretch',icon = ':material/ar_on_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = 'primary' if st.session_state.current_teacher_tab == 'manage_subjects' else 'tertiary'
        if st.button("Manage Subjects",type = type2,width = 'stretch',icon = ':material/book_ribbon:'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3:
        type3 = 'primary' if st.session_state.current_teacher_tab =='attendance_records' else 'tertiary'
        if st.button("Attendance Records",type = type3,width = 'stretch',icon = ':material/cards_stack:'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()   

    if st.session_state.current_teacher_tab == 'take_attendance':
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == 'manage_subjects':
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == 'attendance_records':
        teacher_tab_attendance_records()

    footer_dashboard()

def teacher_tab_take_attendance():
    
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.header("Take AI Attendance")

    if  'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You have not created any subject yet! Please create one to begin!')
        return
    subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}
    
    col1, col2 = st.columns([3,1],vertical_alignment = 'bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options = list(subject_options.keys()))

    with col2:
        if st.button("Start Attendance",icon = ":material/photo_prints:",type = 'primary',width = 'stretch'):
            selected_subject_code = subjects[list(subject_options.keys()).index(selected_subject_label)]['subject_code']
            add_photo_dialog(selected_subject_code)

    selected_subject_id = subject_options[selected_subject_label]
    st.divider()
    if st.session_state.attendance_images:
        st.header("Added Photos")
        gallery_cols = st.columns(4)
        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch',caption = f'Photo {idx+1}')
    has_photos = bool(st.session_state.attendance_images)
    c1,c2,c3 = st.columns(3)

    with c1:
        if st.button("Clear all photos",type = 'tertiary',width = 'stretch',icon = ':material/delete:',disabled = not has_photos):
            st.session_state.attendance_images = []
            st.rerun()
    with c2:
        has_photos = bool(st.session_state.attendance_images)
        if st.button("Run Face Analysis", type = 'secondary', width = 'stretch',icon = ':material/analytics:',disabled = not has_photos):
            st.spinner("Deep Scanning Classroom Photos.....")
            all_detected_id= {}

            for idx, img in enumerate(st.session_state.attendance_images):
                img_np = np.array(img.convert('RGB'))
                detected, _, _, _ = predict_attendance(img_np)

                if detected:
                    for sid in detected.keys():
                        student_id = int(sid)
                        all_detected_id.setdefault(student_id,[]).append(f"Photo {idx+1}")
            
            enrolled_res = supabase.table('subject_students').select("*,students(*)").eq("subject_id", selected_subject_id).execute()

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning("No students enrolled in this course")
            else:
                results, attendance_to_log = [],[]
                current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                for node in enrolled_students:
                    student = node['students']
                    sources = all_detected_id.get(int(student['student_id']),[]) 
                    is_present = len(sources)>0
                    results.append({
                        "Name":student['name'],
                        "ID": student['student_id'],
                        "Sources": ",".join(sources) if is_present else "-",
                        "Status": "✅ Present" if is_present else "❌ Absent"
                    })

                    attendance_to_log.append({
                        'student_id': student['student_id'],
                        'subject_id': selected_subject_id,
                        'timestamp': current_timestamp,
                        'is_present':bool(is_present)
                    })
                attendance_result_dialog(pd.DataFrame(results),attendance_to_log)



                    

        with c3:
            if st.button("Use Voice Attendance", type = 'primary', width = 'stretch',icon = ':material/mic:'):
                voice_attendance_dialog(selected_subject_id)



def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data["teacher_id"]

    if st.session_state.pop("subject_created", False):
        st.success("Subject created successfully!")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Manage Subjects")
    with col2:
        if st.button("Add Subject", width="content", icon=":material/add_circle:", type='primary', key="add_subject_btn"):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for i, sub in enumerate(subjects):
            stats = [
                ("👥", "Students", sub["total_students"]),
                ("🕰️", "Classes", sub["Total_classes"])
            ]
            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],
                stats=stats,
            )
            if st.button(
                f"Share Code: {sub['name']}",
                key=f"sharebtn_{sub['subject_code']}_{i}",
                icon=":material/share:"
            ):
                share_subject_dialog(sub["name"], sub["subject_code"])
    else:
        st.info("No subjects found. Please add a subject to start taking attendance.")

def teacher_tab_attendance_records():
    st.header("Attendance Records")
    teacher_id = st.session_state.teacher_data["teacher_id"]
    records = get_attendance_for_teacher(teacher_id)
    if not records:
        st.info("No attendance records found.")
        return
    data = []
    for r in records:
        ts = r['timestamp']

        data.append({
            "ts_group":ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime('%Y-%m-%d %I:%M %p') if ts else "N'A",
            "Subject": r["subjects"]["name"],
            "Subject code":r['subjects']['subject_code'],
            "is_present":bool(r.get('is_present',False))

        })
    
    df = pd.DataFrame(data)

    summary = (
        df.groupby('ts_group').agg(
            Time=('Time','first'),
            Subject=('Subject','first'),
            Subject_Code=('Subject code','first'),
            Present_Count=('is_present','sum'),
            Total_Count=('is_present','count')
        ).reset_index()
    )
    summary['Attendance_Stats'] = (
        "✅ " + summary["Present_Count"].astype(str) + "/"
        + summary["Total_Count"].astype(str) + " Students"
    )
    display_df = (summary.sort_values(by='ts_group', ascending=False)
                  [['Time','Subject','Subject_Code','Attendance_Stats']])
    st.dataframe(display_df, use_container_width=True, hide_index=True)

def login_teacher(teacher_email,teacher_password):
    if not teacher_email or not teacher_password:
        return False
    teacher = teacher_login(teacher_email,teacher_password)

    if teacher:
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True 
        st.session_state.user_role= 'teacher'
        return True
    return False

    
def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm,Email):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False,"All Fields are required!"
    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match"
    if check_teacher_exists(teacher_username): 
        return False,"Username already taken"
    if check_teacher_email_exists(Email): 
        return False,"Email already taken"
    # Add logic to save teacher data to database
    try:
        create_teacher(teacher_username, teacher_pass, teacher_name,Email)
        return True, "Registration successful"
    except Exception as e:
        return False,"Unexpected Error!"
    
  

def teacher_screen_login():
    c1,c2 = st.columns(2,vertical_alignment="center",gap= "xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back To Home",type = 'secondary',key = "loginbackbtn",shortcut = "control+spacebar"):
            st.session_state["login_type"] = None
            st.rerun()

    st.markdown(
    '<h2 style="white-space: nowrap; font-size: 1.6rem;text_alignment = "center";">Login using password</h2>',
    unsafe_allow_html=True
    )
    st.space()
    

    teacher_email = st.text_input("Email",placeholder="Enter your email")
    st.space()
    teacher_password = st.text_input("Password",type = "password",placeholder="Enter your Password")
    st.space()

    st.divider
    st.space()

    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button("Login",icon =":material/passkey:" ,type = 'secondary',width = 'stretch'):
            teacher = login_teacher(teacher_email,teacher_password)
            if teacher:
                st.toast
                st.success("Welcome back!",icon = "👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials")
    with btnc2:
        if st.button("Register", type = 'primary',width = 'stretch',icon =":material/passkey:"):
            st.session_state. teacher_login_type = "register"
            st.rerun()
    st.space()
    
    footer_dashboard()



def teacher_screen_register():
    c1,c2 = st.columns(2,vertical_alignment="center",gap= "xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back To Home",type = 'secondary',key = "loginbackbtn",shortcut = "control+spacebar"):
            st.session_state["login_type"] = None
            st.rerun()

    st.markdown(
    '<h2 style="white-space: nowrap; font-size: 1.6rem;">Register Your Teacher Profile</h2>',
    unsafe_allow_html=True
    )

    st.space()
    
    teacher_username = st.text_input("Username",placeholder="Enter your username")
    st.space()
    teacher_name = st.text_input("Name",placeholder="Enter your name")
    st.space()
    teacher_email = st.text_input("Email",placeholder="Enter your email")
    st.space()
    teacher_password = st.text_input("Password",type = "password",placeholder="Enter your Password")
    st.space()
    teacher_password_confirm = st.text_input("Confirm Password",type = "password",placeholder="Confirm your Password")

    st.divider
    st.space()

    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button("Register now",icon =":material/passkey:" ,type = 'secondary',width = 'stretch'):
            success,message=register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm, teacher_email)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)
    with btnc2:
        if st.button("Login Instead", type = 'primary',width = 'stretch',icon =":material/passkey:"):
            st.session_state. teacher_login_type = "login"
            st.rerun()
        st.space()
    
    footer_dashboard()


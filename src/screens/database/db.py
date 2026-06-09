from src.screens.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username",username).execute()
    return bool(response.data)

def check_teacher_email_exists(email):
    response = supabase.table("teachers").select("email").eq("email",email).execute()
    return bool(response.data)
    
def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())
    

def create_teacher(username,password,name,email):
    data = {"username": username,
            "password": hash_pass(password),
            "name": name,
            "email": email,
            }
    response = supabase.table("teachers").insert(data).execute()
    


def teacher_login(email,password):
    response = supabase.table("teachers").select("*").eq("email",email).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password,teacher['password']):
            return teacher
    return None


def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data


def create_student(new_name,face_embedding = None ,voice_embedding= None):
    data = {'name': new_name,'face_embedding': face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table("students").insert(data).execute()
    return response.data

def create_subject(sub_id,sub_name,teacher_id,sub_section):
    data = {"subject_code":sub_id,"name":sub_name,"section":sub_section,"teacher_id":teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table("subjects").select("*,subject_students(count),attendance_logs(timestamp)").eq("teacher_id",teacher_id).execute()
    subjects = response.data

    for sub in subjects:
        sub['total_students'] = sub.get("subject_students",[{}])[0].get('count',0) if sub.get("subject_students") else 0
        attendance = sub.get("attendance_logs",[])
        unique_sessions = len(set(log["timestamp"] for log in attendance))
        sub['Total_classes'] = unique_sessions
        sub.pop('subject_students',None)
        sub.pop('attendance_logs',None)
    
    return subjects

def enroll_student_to_subject(student_id,subject_id):
    data = {'student_id':student_id,"subject_id":subject_id}
    response = supabase.table("subject_students").insert(data).execute()
    return response.data


def unenroll_student_to_subject(student_id,subject_id):
    data = {'student_id':student_id,"subject_id":subject_id}
    response = supabase.table("subject_students").delete().eq("student_id",student_id).eq("subject_id",subject_id).execute()
    return response.data

def get_student_subjects(student_id):
    response = supabase.table("subject_students").select("*,subjects(*)").eq('student_id',student_id).execute()
    return response.data

def get_student_attendance(student_id):
    response = supabase.table("attendance_logs").select("*,subjects(*)").eq('student_id',student_id).execute()
    return response.data
def create_attendance(logs):
    response = supabase.table("attendance_logs").insert(logs).execute()
    return response.data
    
def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*,subjects!inner(*)").eq("subjects.teacher_id", teacher_id).execute()
    return response.data

import streamlit as st

def subject_card(name, code, section, stats=None):
    stats_html = ""
    if stats:
        for icon, label, value in stats:
            stats_html += f"""
            <div style="
                background: #F8F9FF;
                border: 1px solid #E8EAF6;
                padding: 10px 18px;
                border-radius: 12px;
                display: inline-block;
                margin-right: 10px;
                font-size: 0.88rem;
                color: #3D3D3D;
            ">
                {icon} <strong>{value}</strong> {label}
            </div>"""

    html = f"""
    <div style="
        background: #FFFFFF;
        border: 1px solid #E8EAF6;
        border-left: 5px solid #5C6BC0;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 16px;
        box-shadow: 0 2px 12px rgba(92, 107, 192, 0.08);
    ">
        <div style="margin-bottom: 6px;">
            <span style="
                font-size: 1.3rem;
                font-weight: 700;
                color: #1A1A2E;
            ">{name}</span>
        </div>
        <div style="margin-bottom: 14px;">
            <span style="
                background: #EEF0FF;
                color: #5C6BC0;
                padding: 3px 10px;
                border-radius: 8px;
                font-size: 0.82rem;
                font-weight: 600;
                margin-right: 10px;
            ">Code: {code}</span>
            <span style="
                background: #F3F4F6;
                color: #6B7280;
                padding: 3px 10px;
                border-radius: 8px;
                font-size: 0.82rem;
                font-weight: 500;
            ">Section: {section}</span>
        </div>
        <div>{stats_html}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

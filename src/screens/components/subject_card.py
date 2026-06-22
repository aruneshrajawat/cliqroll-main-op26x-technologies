import streamlit as st

def subject_card(name, code, section, stats=None):
    stats_html = ""
    if stats:
        for icon, label, value in stats:
            stats_html += f"""
            <div style="
                background: #D4DE95;
                border: 1px solid #BAC095;
                padding: 8px 16px;
                border-radius: 10px;
                display: inline-block;
                margin-right: 8px;
                font-size: 0.85rem;
                color: #000000;
                font-family: Outfit, sans-serif;
            ">
                {icon} <strong>{value}</strong> {label}
            </div>"""

    html = f"""
    <div style="
        background: #ffffff;
        border: 1px solid #BAC095;
        border-left: 5px solid #000000;
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    ">
        <div style="margin-bottom: 6px;">
            <span style="
                font-size: 1.25rem;
                font-weight: 700;
                color: #000000;
                font-family: Outfit, sans-serif;
            ">{name}</span>
        </div>
        <div style="margin-bottom: 14px;">
            <span style="
                background: #BAC095;
                color: #000000;
                padding: 3px 10px;
                border-radius: 8px;
                font-size: 0.82rem;
                font-weight: 600;
                margin-right: 8px;
                font-family: Outfit, sans-serif;
            ">Code: {code}</span>
            <span style="
                background: #D4DE95;
                color: #000000;
                padding: 3px 10px;
                border-radius: 8px;
                font-size: 0.82rem;
                font-weight: 500;
                font-family: Outfit, sans-serif;
            ">Section: {section}</span>
        </div>
        <div>{stats_html}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
from agent import generate_outage_updates

st.set_page_config(
    page_title="Customer Outage Comms Drafter",
    page_icon="🚨",
    layout="wide"
)
st.markdown("""

<style>

.stApp {
    background-color: #0f172a !important;
}

header[data-testid="stHeader"] {
    background: transparent;
}

div[data-testid="stToolbar"] {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

h1, h2, h3 {
    color: #ffffff !important;
}

p,
label {
    color: #cbd5e1 !important;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #ffffff !important;
}

[data-testid="stMetric"] {
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 18px;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

.stTextArea textarea {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    border-radius: 10px;
}

.stSelectbox [data-baseweb="select"] {
    background-color: #ffffff !important;
    border-radius: 10px !important;
}

.stSelectbox [data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111827 !important;
}

.stSelectbox [data-baseweb="select"] div {
    color: #111827 !important;
}

.stSelectbox [data-baseweb="select"] span {
    color: #111827 !important;
    font-weight: 600 !important;
}

.stSelectbox input {
    color: #111827 !important;
}

.stSelectbox svg {
    fill: #111827 !important;
}

div[role="listbox"] {
    background-color: #ffffff !important;
}

div[role="option"] {
    background-color: #ffffff !important;
    color: #111827 !important;
    font-weight: 600 !important;
}

div[role="listbox"] {
    background-color: #1e293b !important;
}

div[role="option"] {
    color: #ffffff !important;
    background-color: #1e293b !important;
}

.stButton button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(90deg, #22c55e, #14b8a6);
    color: #ffffff !important;
    font-size: 16px;
    font-weight: bold;
}

.stDownloadButton > button {
    width: 100%;
    height: 50px;
    border: none;
    border-radius: 10px;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: #ffffff !important;
    font-weight: bold;
}

.stMarkdown {
    color: #f8fafc !important;
}

</style>

""", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(135deg,#0f172a,#1e293b);
padding:30px;
border-radius:18px;
border:1px solid #475569;
margin-bottom:20px;
">

<h1 style="color:white;margin:0;">
🚨 Customer Outage Communications Drafter
</h1>

<p style="
color:#94a3b8;
font-size:18px;
margin-top:10px;
">
AI-Powered Production Support Communication Assistant
</p>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="AI Model",
        value="Gemini 2.5"
    )

with col2:
    st.metric(
        label="Updates Generated",
        value="3"
    )

with col3:
    st.metric(
        label="Agent Status",
        value="Active"
    )
st.markdown("""
<div style="
background:#111827;
padding:15px;
border-radius:12px;
border:1px solid #334155;
margin-bottom:20px;
">

<b style="color:#22c55e;">
● System Status: Operational
</b>

<span style="color:#94a3b8;">
 | AI Agent Active | Communication Engine Ready
</span>

</div>
""", unsafe_allow_html=True)

if "timeline" not in st.session_state:
    st.session_state.timeline = ""

if st.button("📄 Load Sample Incident"):
    st.markdown("""
<div style="
background:#111827;
padding:15px;
border-radius:12px;
border:1px solid #334155;
margin-bottom:20px;
">

🤖 AI Agent automatically analyzes outage severity and generates
customer-friendly communications using Gemini 2.5 Flash.

</div>
""", unsafe_allow_html=True)

    st.session_state.timeline = """
10:05 Database cluster unavailable
10:12 Root cause identified
10:30 Failover initiated
10:45 Recovery in progress
11:00 Service restored
"""

with st.container():

    st.markdown("""
    <div style="
    background:#111827;
    padding:15px;
    border-radius:15px;
    border:1px solid #334155;
    margin-bottom:15px;
    ">
    <h3 style="color:white;">📋 Technical Timeline</h3>
    </div>
    """, unsafe_allow_html=True)

    timeline = st.text_area(
        "",
        height=320,
        value=st.session_state.timeline
    )


with st.sidebar:

    st.header("⚙️ Incident Configuration")

    st.markdown("---")

    severity = st.selectbox(
        "Incident Severity",
        ["Low", "Medium", "High", "Critical"]
    )

    tone = st.selectbox(
        "Communication Tone",
        ["Calm", "Empathetic", "Concise"]
    )

    st.markdown("---")
    st.success("🤖 Gemini 2.5 Flash")
    

if st.button("Generate Drafts"):

    if timeline.strip() == "":
        st.error("Please enter a timeline.")

    else:

        with st.spinner("Generating customer communications..."):

            result = generate_outage_updates(
                timeline,
                severity,
                tone
            )
            from agent import analyze_severity
            detected_severity = analyze_severity(timeline)
        if detected_severity == "Critical":
           st.error(f"🚨 Detected Severity: {detected_severity}")

        elif detected_severity == "High":
            st.warning(f"⚠️ Detected Severity: {detected_severity}")

        else:
           st.success(f"✅ Detected Severity: {detected_severity}")
        

        st.success("Drafts Generated Successfully!")
        
        st.markdown("""
        <h1 style='color:white;'>
         📋 Generated Customer Communications</h1>
         """, unsafe_allow_html=True)

        st.download_button(
        label="📥 Download Generated Updates",data=result,
        file_name="customer_outage_updates.txt",
        mime="text/plain")
        sections = result.split("===")

        if len(sections) >= 3:
         with st.container(border=True):
             st.markdown(
            "<h2 style='color:white;'>📢 Initial Update</h2>",
             unsafe_allow_html=True
               )
             st.write(sections[0])

         with st.container(border=True):
             st.markdown(
             "<h2 style='color:white;'>🔄 In Progress Update</h2>",
              unsafe_allow_html=True)
             st.write(sections[1])

         with st.container(border=True):
             st.markdown(
             "<h2 style='color:white;'>✅ Resolved Update</h2>",
              unsafe_allow_html=True)
             st.write(sections[2])
        

        else:
            st.write(result)
        

        st.markdown("---")
        st.markdown("---")
        st.markdown("""
         <div style="
         text-align:center;
         color:#cbd5e1;
        padding:10px;
        font-size:14px;">
         🚨 Customer Outage Communications Drafter • Powered by Gemini 2.5 Flash • Production Support AI Assistant
         </div>
          """, unsafe_allow_html=True)
        
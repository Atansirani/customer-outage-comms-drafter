import streamlit as st
from agent import generate_outage_updates

st.set_page_config(
    page_title="Customer Outage Comms Drafter",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Customer Outage Comms Drafter")

st.write(
    "Convert technical outage timelines into customer-friendly communication drafts."
)

timeline = st.text_area(
    "Paste Technical Timeline",
    height=200,
    placeholder="""
10:05 Database cluster unavailable
10:12 Root cause identified
10:30 Failover initiated
10:45 Recovery in progress
11:00 Service restored
"""
)

severity = st.selectbox(
    "Select Severity",
    ["Low", "Medium", "High", "Critical"]
)

tone = st.selectbox(
    "Select Tone",
    ["Calm", "Empathetic", "Concise"]
)

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

        st.success("Drafts Generated Successfully!")

        sections = result.split("===")

        if len(sections) >= 3:

            st.subheader("📢 Initial Update")
            st.info(sections[0])

            st.subheader("🔄 In Progress Update")
            st.warning(sections[1])

            st.subheader("✅ Resolved Update")
            st.success(sections[2])

        else:
            st.write(result)
        else:
    st.write(result)

    st.markdown("---")
    st.caption("AI-Powered Customer Outage Communications Drafter")
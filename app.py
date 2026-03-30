import streamlit as st
from agent.graph import generate_proposal

# Load template
with open("templates/proposal.txt", "r") as f:
    template = f.read()

st.title("🤖 AI Proposal Generator")

st.markdown("### 📝 Project Details")

project_description = st.text_area("1. What is the project about?")
client_problem = st.text_area("2. What problem is the client facing?")
your_solution = st.text_area("3. What solution are you offering?")
timeline = st.text_input("4. Timeline / urgency")
your_experience = st.text_area("5. Your experience or proof")

st.markdown("### ⚙️ Settings")

tone = st.selectbox("Tone", ["Professional", "Friendly", "Confident"])

if st.button("Generate Proposal"):
    if project_description and client_problem:
        proposal = generate_proposal(
            template,
            project_description,
            client_problem,
            your_solution,
            timeline,
            your_experience,
            tone
        )
        st.session_state["proposal"] = proposal

if "proposal" in st.session_state:
    st.subheader("Generated Proposal")
    st.text_area("", st.session_state["proposal"], height=400)

    st.download_button(
        label="Download Proposal",
        data=st.session_state["proposal"],
        file_name="proposal.txt",
        mime="text/plain"
    )
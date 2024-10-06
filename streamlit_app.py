import streamlit as st
import os
from openai import OpenAI
import time

# Get API key from Streamlit secrets
aiml_api_key = st.secrets["aiml_api_key"]  # Ensure this is set up in your secrets.toml file
base_url = "https://api.aimlapi.com/v1"  # Assuming this is the correct base URL for API requests

# Initialize OpenAI client with api_key and base_url
client = OpenAI(
    api_key=aiml_api_key,
    base_url=base_url
)

# Function to simulate typing delay
def typing_animation(text, delay=0.05):
    """Simulates a typing animation by printing one character at a time."""
    for letter in text:
        st.markdown(letter, unsafe_allow_html=True)
        time.sleep(delay)

# Space Exploration Chatbot Prompt
def generate_space_chatbot_response(user_input):
    prompt = f"""
    You are a space exploration assistant. Answer the following question in detail, focusing on planets, stars, space missions, or NASA's history:
    Question: {user_input}
    """
    chat_completion = client.chat.completions.create(
        model="o1-mini",  # You can change this to "o1-preview" if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return chat_completion.choices[0].message.content

# Satellite Data Summarizer Prompt
def summarize_satellite_data(data):
    prompt = f"""
    Summarize the following satellite data into an understandable insight for the public, focusing on key changes or trends related to space, earth monitoring, or atmospheric conditions:
    {data}
    """
    chat_completion = client.chat.completions.create(
        model="o1-mini",  # You can change this to "o1-preview" if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return chat_completion.choices[0].message.content

# Create a session state variable to store the chat messages.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar: Space Exploration Chatbot Interface
st.sidebar.title("👨‍🚀 Curious About NASA's Missions? Ask Your Space Guide!")
st.sidebar.write("🌌 Ask me anything about 🪐 planets, stars, NASA's history, or space missions!")

# Predefined questions in the sidebar
st.sidebar.write("### Suggested Questions:")
if st.sidebar.button("What is the Artemis mission?"):
    user_input = "What is the Artemis mission?"
elif st.sidebar.button("Tell me about the Hubble Space Telescope."):
    user_input = "Tell me about the Hubble Space Telescope."
elif st.sidebar.button("What are the moons of Jupiter?"):
    user_input = "What are the moons of Jupiter?"
elif st.sidebar.button("Who was the first person to walk on the Moon?"):
    user_input = "Who was the first person to walk on the Moon?"
elif st.sidebar.button("Explain the significance of the Voyager missions."):
    user_input = "Explain the significance of the Voyager missions."
else:
    user_input = st.sidebar.text_input("Or type your own question here...")

if user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Display the user's message
    with st.sidebar:
        st.markdown(f"**User**: {user_input}")

    # Show a "generating" spinner while the AI is processing the response
    with st.sidebar.spinner("Generating response..."):
        # Generate a response using the Space Exploration Chatbot Prompt
        assistant_reply = generate_space_chatbot_response(user_input)

        # Store the assistant response in session state
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

        # Display the AI's response
        with st.sidebar:
            st.markdown(f"**Assistant**: {assistant_reply}")

# Main: Satellite Data Summarizer
st.title("🌍 Satellite Insights: Understand Earth from Above")
st.subheader("🛰️ Decode Satellite Data for a Clearer View of Our World")
st.markdown("🔭 Our app is designed to support space researchers by providing powerful tools to summarize and analyze satellite data for their studies. Whether you're exploring planetary missions, star systems, or working on space predictions, the Satellite Insights Summarizer translates complex data into actionable insights. Meanwhile, the Space Exploration Chatbot answers questions about NASA’s missions, planets, and stars, offering accurate and detailed information to enhance your research and help you make data-driven predictions.")

uploaded_file = st.file_uploader("Upload Satellite Data File (CSV or JSON)", type=["csv", "json"])
st.write("Upload a CSV or JSON file with satellite data to get a simple, understandable summary.")
if uploaded_file is not None:
    try:
        # Read the data file
        data = uploaded_file.read().decode('utf-8')
        st.subheader("Raw Data")
        st.code(data[:1000] + '...')  # Display a snippet of the data

        if st.button("Summarize Data"):
            with st.spinner('Summarizing...'):
                summary = summarize_satellite_data(data)
            st.subheader("Summary")
            st.write(summary)
    except Exception as e:
        st.error(f"An error occurred: {e}")


# CSS for NASA-Inspired styling and animations + Left-align buttons
st.markdown("""
<style>
    /* Background with a subtle space theme */
    body {
        background: url(https://www.nasa.gov/sites/default/files/thumbnails/image/pia24552-16.jpg) no-repeat center center fixed;
        background-size: cover;
        color: white;
    }
    
    /* Chatbot and satellite UI styling */
    .sidebar .sidebar-content {
        background-color: rgba(0, 0, 50, 0.8); /* Space dark blue */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
    }
    
    .css-1cpxqw2 {
        background-color: rgba(0, 0, 80, 0.8) !important;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px;
        transition: all 0.3s ease-in-out;
        text-align: left; /* Left-align buttons */
    }
    
    .css-1cpxqw2:hover {
        background-color: rgba(50, 50, 255, 0.8) !important;
        transform: scale(1.05);
        color: white;
    }
    
    /* Custom buttons with glow effects */
    .stButton > button {
        background-color: #1e90ff;
        color: white;
        border-radius: 10px;
        transition: all 0.3s ease-in-out;
        text-align: left; /* Left-align buttons */
    }
    
    .stButton > button:hover {
        background-color: #4682b4;
        box-shadow: 0 0 20px #1e90ff;
        transform: scale(1.05);
    }

    /* Input fields for typing */
    input {
        background-color: rgba(0, 0, 80, 0.8);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px;
    }

    /* Smooth fade-in effect for elements */
    .stApp {
        animation: fadeIn 1s ease-in-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
""", unsafe_allow_html=True)

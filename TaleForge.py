import streamlit as st
import os
import openai
import re
import time
import random

# Set page config before other imports
wide_mode = False  # Set to True to enable wide mode
layout_mode = "wide" if wide_mode else "centered"
st.set_page_config(page_title="TaleForge", page_icon="⚒️", layout=layout_mode, initial_sidebar_state="collapsed")

# Set the OpenAI API key directly
#api_key = st.secrets["OPENAI_API_KEY"]
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

def get_unique_themes():
    return [
        "fantasy",
        "sci-fi",
        "horror",
        "mystery",
        "historical fiction",
        "superhero",
        "dystopian",
        "post-apocalyptic",
        "cyberpunk",
        "steampunk",
        "paranormal romance",
        "crime noir",
        "zombie apocalypse",
        "pirate adventure",
        "space opera",
    ]

def get_character_name():
    character_name = st.text_input("Enter your character's name:")
    return character_name

# Function to call the ChatGPT API
def generate_response(user_choice, conversation_history):
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    message_placeholder = st.empty()

    # Animate "Generating your story..." message
    for i in range(3):
        message_placeholder.text("Generating your story" + "." * (i % 4))
        time.sleep(0.5)

    prompt = f"{conversation_history}User chose option {user_choice}. Generate a cohesive and engaging plot that keeps the user intrigued. Second person. Create dramatic situations and make it possible for the user to die if they choose the wrong choice, thus ending the game early. Provide 2 paragraphs of continuation of the story and 4 new choices for the user's next action. Please ensure each choice is on a new line.\n\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=1,
    )

    progress_bar.progress(100)
    time.sleep(0.5)
    message_placeholder.text("Story generated!")
    time.sleep(0.5)

    story, choices = response.choices[0].text.strip().split('\n\n', 1)

    progress_placeholder.empty()
    message_placeholder.empty()

    return story, choices


# Function to generate the initial setting, situation, and character
def generate_initial_scenario():
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    message_placeholder = st.empty()
    message_placeholder.text("Generating initial scenario...")

    # Incorporate the selected genre into the initial prompt
    genre = st.session_state.theme
    initial_prompt = f"Create a connected setting, situation, and character in a {genre} land. The user is the character. Second person. Describe it in 2 or 3 paragraphs and give 4 choices in a list for user's next action."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=initial_prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=1,
    )

    progress_bar.progress(100)
    time.sleep(0.5)
    message_placeholder.text("Initial scenario generated!")
    time.sleep(0.5)

    initial_scenario = response.choices[0].text.strip()
    story, choices = initial_scenario.split('\n\n', 1)

    progress_placeholder.empty()
    message_placeholder.empty()

    return story, choices


# Function to condense conversation history
def condense_history(history):
    condensed_history = []
   
    for text in history:
        # Only remove leading and trailing whitespace
        text = text.strip()
        condensed_history.append(text)
    return "\n\n".join(condensed_history[::-1])

# Initialize session state if not exists
if "on_splash_page" not in st.session_state:
    st.session_state.on_splash_page = True

# Splash page
if st.session_state.on_splash_page:
    st.markdown("<h1 style='text-align: center;'>⚒️ Welcome to TaleForge 📚</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>Welcome to TaleForge, the interactive storytelling experience where you get to create your own adventure and craft a unique story that has never been made before. With the help of OpenAI's language model, your choices will lead you down a path full of surprises and adventure. Let's get started and see where your journey takes you! 🌟</p>
    """, unsafe_allow_html=True)

    st.session_state.character_name = get_character_name()
    st.session_state.theme = st.selectbox("Select a theme for your adventure:", get_unique_themes())

    if st.session_state.character_name and st.button("Begin Adventure"):
        st.session_state.on_splash_page = False
        initial_story, initial_choices = generate_initial_scenario()
        st.session_state.conversation_history = [initial_story]
        st.session_state.choices = initial_choices
        st.experimental_rerun()


if not st.session_state.on_splash_page:
    # Streamlit App

    # Welcome message
    st.markdown("<h1 style='text-align: center; margin-top: -20px;'>⚒️ TALEFORGE 📚</h1>", unsafe_allow_html=True)

    st.write("")  # Add some spacing

    # Define tabs
    tabs = st.tabs(["Story", "History", "About"])

    with tabs[0]:
        # Display the latest response
        st.subheader(f"{st.session_state.character_name}'s Story Unfolds...")
        st.write(st.session_state.conversation_history[0])

        st.write("")  # Add some spacing

        # Display choices
        st.write(st.session_state.choices)

        st.write("")  # Add some spacing

        # Emoji buttons
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
        button_1 = col1.button(" 1️⃣ ", key='button1', help="Choose option 1")
        button_2 = col2.button(" 2️⃣ ", key='button2', help="Choose option 2")
        button_3 = col3.button(" 3️⃣ ", key='button3', help="Choose option 3")
        button_4 = col4.button(" 4️⃣ ", key='button4', help="Choose option 4")
        reset_button = col5.button(" 🔄 ", key='reset_button', help="Reset the story")
        quit_button = col6.button(" 🎬 ", key='quit_button', help="End the story")

        st.write("")  # Add some spacing

        # Custom location for the progress bar
        progress_col, _ = st.columns([1, 3])
        progress_placeholder = progress_col.empty()

    # Handle button actions
    user_choice = None
    if button_1:
        user_choice = 1
    elif button_2:
        user_choice = 2
    elif button_3:
        user_choice = 3
    elif button_4:
        user_choice = 4

    if user_choice:
        # Generate a response
        condensed_history = condense_history(st.session_state.conversation_history)
        response_story, response_choices = generate_response(user_choice, condensed_history)

        # Update the conversation history and choices
        st.session_state.conversation_history.insert(0, response_story)
        st.session_state.choices = response_choices

        # Rerun to display the latest response
        st.experimental_rerun()

    if reset_button:
        st.session_state.conversation_history = []
        st.session_state.on_splash_page = True
        st.experimental_rerun()

    if quit_button:
        st.write(f"Thank you for playing {st.session_state.character_name}! Your story has come to an end. 🎬")
        st.balloons()
        st.stop()

    with tabs[1]:
        st.subheader("🔍 Conversation History")
        for i, history_item in enumerate(st.session_state.conversation_history[::-1]):
            st.write(f"Step {i+1}:")
            st.write(history_item)
            st.write("")  # Add some spacing

    with tabs[2]:
        st.subheader("🎉 About TaleForge")
        st.markdown("""
            Hi there, I'm David Di-Benedetto, the creator of TaleForge! I'm passionate about bringing ideas to life and designing interactive experiences that captivate and entertain. With the power of OpenAI's GPT-3, I've created this web app to provide you with a unique, immersive adventure where your choices shape the narrative.
           
            When I'm not busy working on TaleForge, I love exploring new ideas and creating amazing projects that spark curiosity and inspiration. I invite you to check out my website at [daviddi-benedetto.com](https://daviddi-benedetto.com) to see what else I've been up to. You'll find a collection of my work ranging from creative instruments to aerospace, and much more.
           
            I hope you enjoy your time in TaleForge, and I'd love to hear your thoughts or feedback (daviddi-benedetto@outlook.com). Happy adventuring!
        """)

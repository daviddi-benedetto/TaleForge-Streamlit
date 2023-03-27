import openai
import streamlit as st
import re

# Set the OpenAI API key directly
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to call the ChatGPT API
def generate_response(user_choice, conversation_history):
    prompt = f"{conversation_history}User chose option {user_choice}. Generate a cohesive and engaging plot that keeps the user intrigued. Second person. Create dramatic situations and make it possible for the user to die if they choose the wrong choice, thus ending the game early. Provide 2 paragraphs of continuation of the story and 4 new choices for the user's next action. Please ensure each choice is on a new line.\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=1,
    )
    story, choices = response.choices[0].text.strip().split('\n\n', 1)
    return story, choices

# Function to generate the initial setting, situation, and character
def generate_initial_scenario():
    initial_prompt = "Create a connected setting, situation, and character in a fantasy land. The user is the character. Second person. Describe it in 2 or 3 paragraphs and give 4 choices in a list for user's next action."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=initial_prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=1,
    )
    initial_scenario = response.choices[0].text.strip()
    story, choices = initial_scenario.split('\n\n', 1)
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
if "conversation_history" not in st.session_state:
    initial_story, initial_choices = generate_initial_scenario()
    st.session_state.conversation_history = [initial_story]
    st.session_state.choices = initial_choices

# Streamlit App
# Set page config
wide_mode = False  # Set to True to enable wide mode
layout_mode = "wide" if wide_mode else "centered"
st.set_page_config(page_title="TaleForge", page_icon="📚", layout=layout_mode, initial_sidebar_state="collapsed")


# Welcome message
st.markdown("<h1 style='text-align: center;'>🧙‍♂️ TALEFORGE 📖</h1>", unsafe_allow_html=True)
st.markdown("""
    Welcome to TaleForge! In this interactive storytelling experience, you get to choose your own adventure by selecting one of the given choices.
    Enjoy your unique story. 🌟
""")

# Define tabs
tabs = st.tabs(["Story", "History", "About"])

# Define content for each tab
with tabs[0]:
    # Display the latest response
    st.subheader("🌅 The Story Unfolds...")
    st.write(st.session_state.conversation_history[0])

    # Display choices
    st.write(st.session_state.choices)

    # Emoji buttons
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
    button_1 = col1.button(" 1️⃣ ", key='button1', help="Choose option 1")
    button_2 = col2.button(" 2️⃣ ", key='button2', help="Choose option 2")
    button_3 = col3.button(" 3️⃣ ", key='button3', help="Choose option 3")
    button_4 = col4.button(" 4️⃣ ", key='button4', help="Choose option 4")
    reset_button = col5.button(" 🔄 ", key='reset_button', help="Reset the story")
    quit_button = col6.button(" 🎬 ", key='quit_button', help="End the story")

# Handle button actions
user_choice = None
if button_1:
    user_choice = "1"
elif button_2:
    user_choice = "2"
elif button_3:
    user_choice = "3"
elif button_4:
    user_choice = "4"
elif reset_button:
    # Reset the session state
    st.session_state["conversation_history"] = []
    st.session_state["choices"] = ""

    # Generate the initial scenario
    initial_story, initial_choices = generate_initial_scenario()

    # Assign the initial scenario to the session state
    st.session_state.conversation_history.insert(0, initial_story)
    st.session_state.choices = initial_choices

    # Refresh the page
    st.experimental_rerun()
elif quit_button:
    # Generate ChatGPT response to create a natural and dramatic end to the story
    condensed_history = condense_history(st.session_state.conversation_history)
    prompt = f"{condensed_history}The end. Provide a final paragraph to conclude the story in a satisfying and impactful way."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    end_story = response.choices[0].text.strip()

    # Add the final paragraph to the conversation history
    st.session_state.conversation_history.insert(0, end_story)

    # Display the final paragraph
    st.subheader("🎬 The Final Chapter")
    st.write(st.session_state.conversation_history[0])

    # Hide the choices and emoji buttons
    st.session_state.choices = ""
    st.write("Thanks for playing!👋")



# Generate and display ChatGPT
if user_choice is not None:
    # Generate ChatGPT response
    condensed_history = condense_history(st.session_state.conversation_history)
    story_update, new_choices = generate_response(user_choice, condensed_history)

    # Check for game-ending scenarios
    if "GAME OVER" in story_update.upper():
        st.session_state.conversation_history.insert(0, story_update)
        st.write("You have died, and the game has ended. Better luck next time!")
        quit_button = st.button("Quit")
        if quit_button:
            st.write("Thanks for playing! Goodbye! 👋")
            st.stop()
    else:
        # Add story update to conversation history
        st.session_state.conversation_history.insert(0, story_update)

        # Update choices
        st.session_state.choices = new_choices

        # Refresh the page to update chat history and choices
        st.experimental_rerun()


# Define content for the History tab
with tabs[1]:
    # Display the conversation history
    st.subheader("📜 Your Story")
    for i, response in enumerate(reversed(st.session_state.conversation_history)):
        st.write(f"{response}")

with tabs[2]:
    st.subheader("🎉 About TaleForge")
    st.markdown("""
        Hi there, I'm David Di-Benedetto, the creator of TaleForge! I'm passionate about bringing ideas to life and designing interactive experiences that captivate and entertain. With the power of OpenAI's GPT-3, I've created this web app to provide you with a unique, immersive adventure where your choices shape the narrative.
        
        When I'm not busy working on TaleForge, I love exploring new ideas and creating amazing projects that spark curiosity and inspiration. I invite you to check out my website at [daviddi-benedetto.com](https://daviddi-benedetto.com) to see what else I've been up to. You'll find a collection of my work ranging from creative instruments to aerospace, and much more.
        
        I hope you enjoy your time in TaleForge, and I'd love to hear your thoughts or feedback (daviddi-benedetto@outlook.com). Happy adventuring!
    """)


### TaleForge ###
# Made by David Di-Benedetto

### Imports ---------------------------------------------------------------
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


### Splash Page Interactions -----------------------------------------------
# Your Name
def get_character_name():
    character_name = st.text_input("🧙‍♂️ Enter your character's name:")
    return character_name

# Choose a Role
def get_unique_story_types():
    return [
        "Random 🎲", "Hero 🦸‍♂️🦸‍♀️", "Mentor 🧑‍🏫", "Sidekick 🐶", "Sage 🧙‍♂️🧙‍♀️", 
        "Innocent 😇", "Explorer 🌍", "Rebel 🤘", "Jester 🤡", "Lover ❤️", 
        "Caregiver 🤱", "Creator 🎨", "Destroyer 💥", "Magician 🎩", "Ruler 👑", 
        "Trickster 🃏", "Outlaw 🏴‍☠️", "Scapegoat 🐐", "Villain 😈", "Anti-Hero 🦹‍♂️🦹‍♀️", 
        "Warrior ⚔️", "Thief 🦝", "Femme Fatale 💄", "Damsel in Distress 👧", "Wise Old Man/Woman 👴👵", 
        "Mad Scientist 🧪", "Detective 🕵️‍♂️🕵️‍♀️", "Everyman/Everywoman 👨‍👩‍👧‍👦", "Con Artist 🕵️‍♂️", "Lone Wolf 🐺", 
        "Orphan 😔", "Sinner 😈", "Saint 😇", "Coward 🐔", "Martyr 🙏", 
        "Clown 🤡", "Snob 🧐", "Charmer 😍", "Good Samaritan 🙏", "Seducer 😘", 
        "Boss 👔", "Henchman 👥", "Revolutionary ✊", "Priest ⛪", "Soldier 🎖️", 
        "Wanderer 🚶", "Survivor 🌟", "Loner 🧍", "Misfit 🤪", "Addict 💉", 
        "Visionary 🌟", "Nurturer 🤱", "Enigma ❓", "Temptress 😈", "Crusader 🏰", 
        "Artist 🎨", "Idealist 💭", "Realist 👀", "Analyst 🧐", "Entrepreneur 💼", 
        "Opportunist 💰", "Escapist 🌟", "Prophet 📖", "Healer 🧑‍⚕️", "Protector 🛡️", 
        "Avenger 🔪", "Trickster Hero 🦊", "Savior 🙏", "Redeemer 🙌", "Guardian 🛡️", 
        "Liberator 🌟", "Dreamer 💭", "Loyalist 🤝", "Vengeful 🔪", "Leader 👑", 
        "Innovator 🔬", "Empath 🤝", "Listener 👂", "Mentor's Shadow 👤", "Seeker 🔍", 
        "Neutral 🤷", "Reluctant Hero 😕", "Shadow 👥", "Adversary 😠", "Monster 👹", 
        "Survivor 🌟", "Outcast 🚪", "Dark Lord 🦹"]


# Choose a Theme
def get_unique_themes():
    return ["Random 🎲", "Fantasy 🧙‍♂️", "Sci-Fi 🚀", "Horror 🧟‍♂️", "Mystery 🕵️‍♂️", "Historical Fiction 🏰", "Superhero 🦸‍♂️",
            "Dystopian 🌆", "Post-Apocalyptic 🌍", "Cyberpunk 🤖", "Steampunk ⚙️", "Paranormal Romance 👻",
            "Crime Noir 🕵️‍♂️", "Zombie Apocalypse 🧟‍♂️", "Pirate Adventure 🏴‍☠️", "Space Opera 🚀",
            "Time Travel ⏰", "Alternate History 🕰️", "Survival 🏞️", "War ⚔️", "Comedy 🤣",
            "Action/Adventure ⚔️", "Romantic Comedy ❤️🤣", "Gothic 🦇", "Fairy Tale 🧚", 
            "Epic Fantasy 🐉", "Apocalyptic 🌍", "Alien Invasion 👽", "Artificial Intelligence 🤖",
            "Drama 🎭", "Mythology 🏛️", "Urban Fantasy 🏙️", "Historical Fantasy 🏰", "Space Western 🤠",
            "Military Science Fiction 🎖️", "Soft Science Fiction 🚀", "Hard Science Fiction 🚀", 
            "Contemporary Fantasy 🏙️", "Dark Fantasy 🖤", "Sword and Sorcery ⚔️", "Stealth Action 🕵️‍♂️",
            "Spy Fiction 🕵️‍♂️", "Sports Fiction 🏀", "Speculative Fiction 🤔", "Alternate Universe 🌎",
            "Erotic Romance 🔥", "New Weird 🤪", "Drama-Romance 🎭❤️", "Historical Romance 💕",
            "Young Adult 🧑‍🎓", "Comedy-Drama 🤣🎭", "Slice of Life 🌳", "Psychological Thriller 🧠🕵️‍♂️",
            "Political Thriller 🏛️🕵️‍♂️", "Coming-of-Age 🧑‍🎓", "Teen Romance 💕🧑‍🎓", "Teen Comedy 🤣🧑‍🎓",
            "Medical Drama 🏥", "Disaster Movie 🌪️", "Survival Horror 🧟‍♂️🌳", "Creature Feature 🐲",
            "Military Thriller 🎖️🕵️‍♂️", "Legal Drama ⚖️", "Courtroom Thriller ⚖️🕵️‍♂️", "Heist 💰",
            "Gangster 🕵️‍♂️", "Psychological Horror 🧠👻", "Supernatural Thriller 👻🕵️‍♂️",
            "Political Satire 🏛️🤣", "Existential Drama 🧐🎭", "Surrealism 🤪", "Postmodernism 🕰️🤪",
            "Magical Realism", "Absurdist Comedy 🤪🤣", "Documentary-style 📷", "Found Footage 📹", "Mockumentary 🤣📹",
            "Musical Comedy 🎶🤣", "Science Fiction Horror 🧟‍♂️🚀", "Steampunk Romance 💕⚙️",
            "Slasher 🔪", "Monster Movie 🐲", "Disaster Thriller 🌪️🕵️‍♂️", "Alien Abduction 👽",
            "Robotics and AI 🤖", "Space Horror 👽🚀", "Cyber-Thriller 🤖🕵️‍♂️", "Military Science Fantasy 🎖️🐉",
            "Techno-Thriller 🕵️‍♂️🤖", "Psychological Drama 🧠🎭", "Eco-Thriller 🌿🕵️‍♂️", "Crime Drama 🕵️‍♂️🎭",
            "Psychological Mystery 🧠🕵️‍♂️", "Historical Epic 🏰🎖️", "War Drama 🎖️🎭", "Postcolonial 🌍🕰️",
            "Martial Arts 🥋", "Underwater Adventure 🏊‍♂️🐠", "Time Loop ⏰", "Mystery Comedy 🕵️‍♂️🤣"
]





### Initial Scenario Generation --------------------------------------------

# Function to generate the initial setting, situation, and character
def generate_initial_scenario():
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    message_placeholder = st.empty()
    message_placeholder.text("Generating initial scenario...")

    # Incorporate the selected genre and character name into the initial prompt
    genre = st.session_state.theme
    story_type = st.session_state.story_type
    initial_prompt = f"Story Genre and Setting:{genre}, Character Role:{story_type} Create the introduction to a long and elaborate CYOA-style story IN SECOND PERSON with a minimum of 3 paragraphs in a connected setting and creative situation. The character's name is {st.session_state.character_name}. Give the world a unique name, history, setting, and describe it to the player. Give CYOA-like open ended suggestions for the user without telling them the outcomes of their actions."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=initial_prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=1,
    )

    progress_bar.progress(100)
    time.sleep(0.5)
    message_placeholder.text("Initial scenario generated!")
    time.sleep(0.5)

    initial_scenario = response.choices[0].text.strip()

    # Replace the placeholder name in the story with the actual character name
    story = initial_scenario.replace("Player", st.session_state.character_name)

    split_scenario = story.split('\n\n', 1)

    if len(split_scenario) == 2:
        story, choices = split_scenario
    else:
        story = split_scenario[0]
        choices = "No choices were generated. Please try again."

    progress_placeholder.empty()
    message_placeholder.empty()

    return story, choices

### Continued Story Generation ---------------------------------------------

# Function to generate the continued story
def generate_response(user_choice, conversation_history):
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    message_placeholder = st.empty()

    # Animate "Generating your story..." message
    for i in range(3):
        message_placeholder.text("Generating your story" + "." * (i % 4))
        time.sleep(0.5)

    prompt = f"{conversation_history}\n- User's action: {user_choice} \n- Task: Repeat to the user what action they took in a story-book way. Make a spacer line. Then, generate a cohesive and engaging plot as a direct continuation from the action the user took that keeps the user intrigued. Genre:{st.session_state.theme}, Character role:{st.session_state.story_type}. Tell the story in second person, with the player being the one addressed. Create a well-written plot and make it possible for the user to die if they choose the wrong action, thus ending the game early. Provide 2 or 3 paragraphs of direct continuation of the story. Give CYOA-like open ended suggestions for the user without telling them the outcomes of their actions at the end."

    # Keep making API calls until choices are generated
    choices_generated = False
    while not choices_generated:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=1,
        )

        split_response = response.choices[0].text.strip().split('\n\n', 1)

        if len(split_response) == 2:
            story, choices = split_response
            choices_generated = True
        else:
            story = split_response[0]
            choices = "No choices were generated. Please try again."

    progress_bar.progress(100)
    time.sleep(0.5)
    message_placeholder.text("Story generated!")
    time.sleep(0.5)

    progress_placeholder.empty()
    message_placeholder.empty()

    st.session_state.user_action = "" # Clear the user input box

    return story, choices


# Get user action
def get_user_action():
    if "clear_input" in st.session_state and st.session_state.clear_input:
        user_action = st.text_input("Enter your action 👉", value="")
        st.session_state.clear_input = False
    else:
        user_action = st.text_input("Enter your action 👉")
    return user_action




# Function to condense conversation history
def condense_history(history):
    condensed_history = []

    for text in history:
        # Only remove leading and trailing whitespace
        text = text.strip()
        condensed_history.append(text)
    return "\n\n".join(condensed_history[::-1])

### Splash Page Creation ---------------------------------------------------

# Initialize session state if not exists
if "on_splash_page" not in st.session_state:
    st.session_state.on_splash_page = True
    st.session_state.conversation_history = []

if "input_box_value" not in st.session_state:
    st.session_state.input_box_value = ""


# Splash page
if st.session_state.on_splash_page:
    st.markdown("<h1 style='text-align: center;'>⚒️ Welcome to TaleForge 📚</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>Embark on an infinite adventure of free will with TaleForge! Create your own unique story with OpenAI's latest language models, and experience a world full of surprises and excitement :)</p>
    """, unsafe_allow_html=True)



    st.session_state.character_name = get_character_name()
    st.session_state.story_type = st.selectbox("🎭 Select a role:", get_unique_story_types())
    st.session_state.theme = st.selectbox("🎨 Select a theme for your adventure:", get_unique_themes())

    if st.session_state.character_name and st.button("Begin Adventure"):
        st.session_state.on_splash_page = False
        initial_story, initial_choices = generate_initial_scenario()
        st.session_state.conversation_history = [initial_story]
        st.session_state.choices = initial_choices
        st.experimental_rerun()

    st.write("")
    st.markdown("""
        <p style='text-align: center;'>Made by <a href='https://daviddi-benedetto.com' target='_blank'>David Di-Benedetto</a></p>
    """, unsafe_allow_html=True)



### Overview ---------------------------------------------------------------
if not st.session_state.on_splash_page:
    # Streamlit App

    # Welcome message
    st.markdown("<h1 style='text-align: center; margin-top: -20px;'>⚒️ TALEFORGE 📚</h1>", unsafe_allow_html=True)

    st.write("")  # Add some spacing

    # Define tabs
    tabs = st.tabs(["Story", "History", "About"])

    with tabs[0]:
        # Display the latest response
        st.subheader(f"{st.session_state.character_name}'s Tale")
        st.write(st.session_state.conversation_history[0])


        # Display choices
        st.write(st.session_state.choices)


        # Get user action
        st.session_state.user_action = get_user_action()

        # Generate the story based on user action
        if st.session_state.user_action:
            if st.button("Submit Action"):
                new_story, new_choices = generate_response(st.session_state.user_action, condense_history(st.session_state.conversation_history))
                st.session_state.conversation_history.insert(0, new_story)
                st.session_state.choices = new_choices
                st.session_state.input_box_value = ""  # Clear the input box value
                st.experimental_rerun()



    with tabs[1]:
        st.subheader("📜 Your Story")
        for history_item in reversed(st.session_state.conversation_history):
            for item in history_item.split('\n\n'):
                st.write("➔", item)
            st.write(st.session_state.choices)  # display choices for each step

    with tabs[2]:
        st.subheader("🎉 About TaleForge")
        st.markdown("""
            Hi there, I'm David Di-Benedetto, the creator of TaleForge! I'm passionate about bringing ideas to life and designing interactive experiences that captivate and entertain. With the power of OpenAI's GPT-3, I've created this web app to provide you with a unique, immersive adventure where your choices shape the narrative.
        
            When I'm not busy working on TaleForge, I love exploring new ideas and creating amazing projects that spark curiosity and inspiration. I invite you to check out my website at [daviddi-benedetto.com](https://daviddi-benedetto.com) to see what else I've been up to. You'll find a collection of my work ranging from creative instruments to aerospace, and much more.
        
            I hope you enjoy your time in TaleForge, and I'd love to hear your thoughts or feedback (daviddi-benedetto@outlook.com). Happy adventuring!
        """)


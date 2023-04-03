### TaleForge ###
# Made by David Di-Benedetto

### Imports ---------------------------------------------------------------
import sys

sys.path.insert(1, "TaleForge/streamlit-option-menu-0.3.2/streamlit_option_menu")

from streamlit_option_menu import option_menu
import streamlit as st
import openai
import time
import webbrowser


### Set wide mode & Page Title ----------------------------------------------------------
st.set_page_config(page_title="TaleForge", page_icon="⚒️", layout = "wide", initial_sidebar_state="expanded")   # must be first command in script

### Custom CSS to style the sidebar and tabs -------------------------------
def custom_css():
    st.markdown(
        """
        <style>
            /* Change the sidebar width */
            .sidebar .sidebar-content {
                width: 50px;
            }

            /* Style the radio buttons as tabs */
            .stRadio > div[role="radiogroup"] > label {
                display: inline-block;
                background-color: #36393F;
                padding: 10px 50px;
                margin: 5px;
                border-radius: 4px;
                cursor: pointer;
            }

            /* Style the selected tab */
            .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child > div:first-child {
                background-color: #2C2F33 !important;
            }

            .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:last-child {
                color: #DCDDDE !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call the custom_css function to apply the custom styles
custom_css()


### Hide Streamlit elements ---------------------------------------------------
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

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
def get_user_action(input_key):
    col1, col2 = st.columns([5, 1])  # Create two columns with a 4:1 ratio

    if "clear_input" in st.session_state and st.session_state.clear_input:
        user_action = col1.text_input("Enter your action 👉", value="", key=input_key)
        st.session_state.clear_input = False
    else:
        user_action = col1.text_input("Enter your action 👉", key=input_key)

    # Add the submit button in the second column with custom CSS for alignment
    submit_button_html = """
        <style>
            .submit_button {
                padding-top: 35px;
            }
        </style>
        <script>
            // Function to handle 'Enter' key press
            function handleEnterKey(event) {
                if (event.key === "Enter") {
                    let form = document.createElement("form");
                    form.style.display = "none";
                    document.body.appendChild(form);
                    form.submit();
                }
            }

            // Attach event listener to the text input field
            setTimeout(function() {
                let inputElements = document.getElementsByTagName("input");
                for (let i = 0; i < inputElements.length; i++) {
                    if (inputElements[i].placeholder === "Enter your action 👉") {
                        inputElements[i].addEventListener("keydown", handleEnterKey);
                    }
                }
            }, 100);
        </script>
        <div class="submit_button">
    """




    col2.markdown(submit_button_html, unsafe_allow_html=True)
    submit_button = st.session_state.input_box_value != user_action
    col2.markdown("</div>", unsafe_allow_html=True)

    if submit_button:
        st.session_state.input_box_value = user_action
        st.session_state.input_key += 1  # Increment the input_key value



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

if "story_generated" not in st.session_state:
    st.session_state.story_generated = False

if "story_started" not in st.session_state:
    st.session_state.story_started = False

if "input_key" not in st.session_state:
    st.session_state.input_key = 0


# Custom CSS for sidebar
st.markdown("""
<style>
    .sidebar .sidebar-content {
        width: 350px !important; /* Adjust the value to your desired fixed width */
    }
</style>
""", unsafe_allow_html=True)

# Define sidebar
sidebar = st.sidebar

with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold;'>TaleForge</h1>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("## 🧭 Navigator", unsafe_allow_html=True)
    page = option_menu("", ["📖 Story", "📜 History", "🔖 About", "📚 How to Play", "⚖️ Terms of Service"])

    # Add the buttons with links directly to the sidebar
    st.markdown("## 🔗 Links")

    if st.button("👥 Patreon"):
        webbrowser.open("https://www.patreon.com/your_username")

    if st.button("☕ Buy Me a Coffee"):
        webbrowser.open("https://www.buymeacoffee.com/your_username")

    if st.button("📺 YouTube"):
        webbrowser.open("https://www.youtube.com/your_channel")

if page == "📖 Story":
    if not st.session_state.story_started:
        # Create columns to center the content
        left_column, center_column, right_column = st.columns([1, 4, 1])  # Adjust the width ratio of the columns

        # Place the content inside the center column
        with center_column:
            st.markdown("<div style='padding: 0 1rem;'><h1 style='text-align: center;'>👋 Welcome!</h1></div>", unsafe_allow_html=True)
            st.markdown("""
                <div style='padding: 0 1rem;'><p style='text-align: center;'>Embark on an infinite adventure of free will with TaleForge! Create your own unique story with OpenAI's latest language models, and experience a world completely unique to you!</p></div>
            """, unsafe_allow_html=True)

            st.session_state.character_name = get_character_name()
            st.session_state.story_type = st.selectbox("🎭 Select a role:", get_unique_story_types())
            st.session_state.theme = st.selectbox("🎨 Select a theme for your adventure:", get_unique_themes())

            if st.session_state.character_name and st.button("Begin Adventure"):
                st.session_state.story_started = True
                initial_story, initial_choices = generate_initial_scenario()
                st.session_state.conversation_history = [initial_story]
                st.session_state.choices = initial_choices
                st.experimental_rerun()

    if st.session_state.story_started:
        # Display the latest response
        st.subheader(f"📖 The Tale of {st.session_state.character_name}")
        st.write(st.session_state.conversation_history[0])

        # Display choices
        st.write(st.session_state.choices)

        # Get user action
        st.session_state.user_action = get_user_action(st.session_state.input_key)

        # Generate the story based on user action
        if st.session_state.user_action:
            new_story, new_choices = generate_response(st.session_state.user_action, condense_history(st.session_state.conversation_history))
            st.session_state.conversation_history.insert(0, new_story)
            st.session_state.choices = new_choices
            st.session_state.user_action = ""  # Clear the user input in the session state
            st.session_state.clear_input = True  # Set clear_input flag to True
            st.experimental_rerun()  # Force a rerun to refresh the input box


elif page == "📜 History":
    st.subheader("📜 Your Story")
    
    # Display the story history
    for history_item in reversed(st.session_state.conversation_history):
        for item in history_item.split('\n\n'):
            st.write("➔ ", item)
        st.write(st.session_state.choices)  # display choices for each step

elif page == "🔖 About":
    st.subheader("🔖 About TaleForge")
    st.markdown("""
        Hi there, I'm David Di-Benedetto, the creator of TaleForge! I'm passionate about bringing ideas to life and designing interactive experiences that captivate and entertain. With the power of OpenAI's GPT-3, I've created this web app to provide you with a unique, immersive adventure where your choices shape the narrative.

        When I'm not busy working on TaleForge, I love exploring new ideas and creating amazing projects that spark curiosity and inspiration. I invite you to check out my website at [daviddi-benedetto.com](https://daviddi-benedetto.com) to see what else I've been up to. You'll find a collection of my work ranging from creative instruments to aerospace, and much more.

        I hope you enjoy your time in TaleForge, and I'd love to hear your thoughts or feedback (daviddi-benedetto@outlook.com). Happy adventuring!
    """)

elif page == "📚 How to Play":
    st.subheader("📚 How to Play TaleForge")
    st.markdown("""
        Welcome to TaleForge! If you're new to the world of interactive storytelling, don't worry – we've got you covered. Follow these simple steps to get started on your unique adventure:

        1. **Character Creation**: Begin by entering a name for your character, selecting a role, and choosing a theme for your adventure on the main '📖 Story' tab.

        2. **Story Introduction**: Once you've set up your character, TaleForge will generate an introduction to your adventure. Read through the scenario, and pay attention to the options provided at the end.

        3. **Making Choices**: After reading the introduction, you'll be presented with a set of choices in the form of open-ended suggestions. To make a choice, simply type your action into the "Enter your action 👉" text input field and press Enter or click outside the input box.

        4. **Continuing the Story**: As you make choices, TaleForge will generate a continuation of the story based on your actions. Be aware that your choices might lead to different outcomes, and in some cases, your character could even die if you choose the wrong action.

        5. **Reviewing Your Adventure**: You can review your entire adventure by visiting the '📜 History' tab. This will display your story in reverse chronological order, allowing you to reflect on your choices and see how the narrative has developed.

        Now that you know the basics, it's time to embark on your very own adventure in TaleForge! Remember, the story is shaped by your choices, so think carefully and enjoy the journey.
    """)

elif page == "⚖️ Terms of Service":
    st.subheader("⚖️ Terms of Service")
    st.markdown("""
        ## Note From The Creator
        
        This app runs on language-based AI, which is incredibly fun to use in the setting of a game, but it can also be unpredictable at times. I've done my best to ensure that the app is safe to use, but please use your best judgement when running prompts through it. I'm not responsible for any inappropriate content that may be generated by the AI. Thank you for your understanding!

        ## Terms of Service

        This is a work of fiction. Names, characters, places, and incidents either are the product of the author's imagination or are used fictitiously. Any resemblance to actual events, locales, or persons, living or dead, is entirely coincidental.
        
        The following terms and conditions govern all use of the TaleForge web application ("the Service") and all content, services, and products available at or through the Service. The Service is owned and operated by David Di-Benedetto ("TaleForge"). The Service is offered subject to your acceptance without modification of all of the terms and conditions contained herein and all other operating rules, policies (including, without limitation, TaleForge's Privacy Policy), and procedures that may be published from time to time on this site by TaleForge (collectively, the "Agreement").

        Please read this Agreement carefully before accessing or using the Service. By accessing or using any part of the Service, you agree to become bound by the terms and conditions of this Agreement. If you do not agree to all the terms and conditions of this Agreement, then you may not access the Service or use any services. If these terms and conditions are considered an offer by TaleForge, acceptance is expressly limited to these terms.

        ## Responsibility of Users

        By using the Service, you represent and warrant that your use of the Service will not infringe the proprietary rights, including but not limited to the copyright, patent, trademark, or trade secret rights, of any third party.

        ## Content Posted on Other Websites

        We have not reviewed, and cannot review, all of the material, including computer software, made available through the websites and webpages to which TaleForge links, and that link to TaleForge. TaleForge does not have any control over those external websites and webpages and is not responsible for their contents or their use.

        ## Copyright Infringement and DMCA Policy

        As TaleForge asks others to respect its intellectual property rights, it respects the intellectual property rights of others. If you believe that material located on or linked to by TaleForge violates your copyright, you are encouraged to notify TaleForge. TaleForge will respond to all such notices, including as required or appropriate by removing the infringing material or disabling all links to the infringing material.

        ## Intellectual Property

        This Agreement does not transfer from TaleForge to you any TaleForge or third-party intellectual property, and all right, title, and interest in and to such property will remain (as between the parties) solely with TaleForge.

        ## Changes

        TaleForge reserves the right, at its sole discretion, to modify or replace any part of this Agreement. It is your responsibility to check this Agreement periodically for changes. Your continued use of or access to the Service following the posting of any changes to this Agreement constitutes acceptance of those changes.

        ## Termination

        TaleForge may terminate your access to all or any part of the Service at any time, with or without cause, with or without notice, effective immediately.

        ## Disclaimer of Warranties

        The Service is provided "as is." TaleForge and its suppliers and licensors hereby disclaim all warranties of any kind, express or implied, including, without limitation, the warranties of merchantability, fitness for a particular purpose, and non-infringement. Neither TaleForge nor its suppliers and licensors makes any warranty that the Service will be error-free or that access thereto will be continuous or uninterrupted. You understand that you download from, or otherwise obtain content or services through, the Service at your own discretion and risk.

        In no event will TaleForge, or its suppliers or licensors, be liable with respect to any subject matter of this Agreement under any contract, negligence, strict liability or other legal or equitable theory for: (i) any special, incidental, or consequential damages; (ii) the cost of procurement for substitute products or services; (iii) for interruption of use or loss or corruption of data; or (iv) for any amounts that exceed the fees paid by you to TaleForge under this Agreement during the twelve (12) month period prior to the cause of action. TaleForge shall have no liability for any failure or delay due to matters beyond their reasonable control. The foregoing shall not apply to the extent prohibited by applicable law.

        You agree to indemnify and hold harmless TaleForge, its contractors, and its licensors, and their respective directors, officers, employees, and agents from and against any and all claims and expenses, including attorneys' fees, arising out of your use of the Service, including but not limited to your violation of this Agreement.
        
        TaleForge reserves the right, at its sole discretion, to modify or replace any part of this Agreement. It is your responsibility to check this Agreement periodically for changes. Your continued use of or access to the Service following the posting of any changes to this Agreement constitutes acceptance of those changes. TaleForge may also, in the future, offer new services and/or features through the Service (including, the release of new tools and resources). Such new features and/or services shall be subject to the terms and conditions of this Agreement.
    """)

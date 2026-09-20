import pandas as pd
import streamlit as st

# Setup player session state for Magic HP and Inventory
if "current_scene" not in st.session_state:
    st.session_state.current_scene = 1

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0

if "inventory" not in st.session_state:
    st.session_state.inventory = []

# Main Adventure Dataframe
story_data = {
    "scene_id": [1, 2, 3, 4, 5],
    "title": [
        "The Rainbow Brick Portal",
        "The Crazy Wizard's Gate",
        "The Well of Lost Pixels",
        "The Crystal Prism Castle",
        "Back to Reality",
    ],
    "story_text": [
        "You get sucked into the terminal of the code you're writing and land hard on a glowing rainbow brick road! Looking down, you spot a stray Jimin photocard on the floor. You pick it up, wondering who dropped it, and head down the path to reach the distant Crystal Prism Castle which will help you get back home.",
        "While walking down the road, you get stopped by a tall, black gate. A crazy Wizard in a sparkly purple robe blocks the archway. He shouts: 'I am the ultimate ARMY! Answer my 5 BTS trivia questions correctly and I will let you through. Answer wrong, I will make you disappear into the Cloud forever!'",
        "Having passed the Wizard, you arrive at the shimmering Well of Lost Pixels. Legend says making a wish here grants an artifact that will help you in unkown ways. You throw in a quarter and make your wish...",
        "Inside the towering Crystal Prism Castle, you find Sage from Valorant, completely encased in green crystal! She whispers: I used the last bit of my energy to summon you here...please save me!",
        "Sage is forever grateful that you saved her. Naturally, you will now be insufferable for the next few days. She uses her restored magic to send a beam of light through the realm. You wake up at your desk in the Computer lab! It was just a crazy dream. You find it hard to believe you could ever meet your favorite agent Sage. You grab some Taco Bell, play BTS in your headphones and boot up Valorant.",
    ],
}

df_story = pd.DataFrame(story_data)

# Quiz Questions for Scene 2
bts_quiz = [
    {
        "q": "Question 1: How many members are in BTS?",
        "options": ["5","7"],
        "correct": "7",
    },
    {
        "q": "Question 2: Who was the very first member recruited to BTS?",
        "options":["RM", "Suga"],
        "correct":"RM",
    },
    {
        "q": "Questions 3: What is V's real name?",
        "options": ["Jung Hoseok","Kim Taehyung"],
        "correct": "Kim Taehyung",
    },
    {
        "q": "Question 4: Who is the youngest member (Golden maknae) in BTS?",
        "options": ["Jungkook (The Great)", "Jimin"],
        "correct": "Jungkook (The Great)",
    },
    {
        "q": "FINAL QUESTION: The Wizard leans in close...'Now tell me, WHO IS MY BIAS?'",
        "options": ["J-Hope","Jimin"],
        "correct": "Jimin",
    },
]

# Sidebar Display
st.sidebar.title("Inventory")
if "Jimin Photocard" in st.session_state.inventory:
    st.sidebar.write("📸 Jimin Photocard")
if "Crystal Smasher Pickaxe" in st.session_state.inventory:
    st.sidebar.write("⛏️ Magical Pickaxe")

if st.sidebar.button("Restart Adventure"):
    st.session_state.current_scene = 1
    st.session_state.quiz_step = 0
    st.session_state.inventory = []
    st.rerun()

# Fetch Current Scene
current_id = st.session_state.current_scene
scene = df_story[df_story["scene_id"] == current_id].iloc[0]

# Scene 1: Rainbow Brick Portal ------------------------------------------------------------
if current_id == 1:
    st.error(f"🌈 {scene['title']}")
    st.write(scene["story_text"])
    if "Jimin Photocard" not in st.session_state.inventory:
        st.session_state.inventory.append("Jimin Photocard")
    if st.button("Walk towards the Gate"):
        st.session_state.current_scene = 2
        st.rerun()

# Scene 2: Wizard Quiz ---------------------------------------------------------------------
elif current_id == 2:
    st.warning(f"🧙 {scene['title']}")
    st.write(scene["story_text"])
    st.divider()

    step = st.session_state.quiz_step
    if step < len(bts_quiz):
        q_data = bts_quiz[step]
        st.subheader(q_data["q"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button(q_data["options"][0]):
                if q_data["options"][0] == q_data["correct"]:
                    st.session_state.quiz_step += 1
                    if st.session_state.quiz_step == 5:
                        st.session_state.current_scene = 3
                    st.rerun()
                else:
                    st.error("WRONG! The Wizard zaps you into thin air!")
                    st.session_state.current_scene = 1
                    st.session_state.quiz_step = 0
                    st.session_state.inventory = []
        with col2:
            if st.button(q_data["options"][1]):
                if q_data["options"][1] == q_data["correct"]:
                    st.session_state.quiz_step += 1
                    if st.session_state.quiz_step == 5:
                        st.session_state.current_scene = 3
                    st.rerun()
                else:
                    st.error("WRONG! The wizard compresses you into a zip file!")
                    st.session_state.current_scene = 1
                    st.session_state.quiz_step = 0
                    st.session_state.inventory = []

# Scene 3: Well of Lost Pixels ---------------------------------------------------------------------------------------
elif current_id == 3:
    st.info(f"✨ {scene['title']}")
    st.write(scene["story_text"])

    if st.button("Wish for a Crystal-breaking Tool"):
        st.success(
            "The well sparkles and spits out a [Crystal Smasher Pickaxe]!"
        )
        if "Crystal Smasher Pickaxe" not in st.session_state.inventory:
            st.session_state.inventory.append("Crystal Smasher Pickaxe")
        st.session_state.current_scene = 4
        st.rerun()
# Scene 4: Crystal Prism Castle ----------------------------------------------------------------------------------------
elif current_id == 4:
    st.success(f"🔮 {scene['title']}")
    st.write(scene["story_text"])

    # Initialize crystal health if it doesn't exist et
    if "crystal_hp" not in st.session_state:
        st.session_state.crystal_hp = 10 # Needs 10 taps to shatter

    if "Crystal Smasher Pickaxe" in st.session_state.inventory:
        st.subheader("⛏️ Shatter the Green Crystal!")

        # Display a progress bar for the crystal breaking
        # (10 taps left = 0% broken, 0 taps left = 100%)
        progress = (10 - st.session_state.crystal_hp) / 10 
        st.progress(progress)

        st.write(f"**Crystal Integrity:** {st.session_state.crystal_hp} HP left")

        if st.session_state.crystal_hp > 0:
            if st.button("⛏️ Tap to swing Pickaxe!"):
                st.session_state.crystal_hp -= 1
                st.rerun()
        else:
            st.success(
                "CRACK! The crystal shatters and Sage is free!"
            )
            if st.button("Talk to Sage"):
                # Reset crystal HP for next playthrough and move to end scene
                st.session_state.crystal_hp = 10
                st.session_state.current_scene = 5
                st.rerun()

# Scene 5: End Game -----------------------------------------------------------------------------------------------------
elif current_id == 5:
    st.success(f"🌮 {scene['title']}")
    st.write(scene["story_text"])

    if st.button("Play Again"):
        st.session_state.current_scene = 1
        st.session_state.quiz_step = 0
        st.session_state.inventory = []
        st.rerun()

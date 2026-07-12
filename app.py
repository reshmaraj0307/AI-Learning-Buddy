import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------
# GEMINI CLIENT
# -----------------------------------
@st.cache_resource
def get_client():

    return genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------


# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("🎓 AI Learning Buddy")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📖 Learn",
        "📝 Quiz",
        "✅ Feedback",
        "ℹ About"
    ]
)

# -----------------------------------
# HOME PAGE
# -----------------------------------
if page == "🏠 Home":

    st.markdown("""
    <div class="hero-section">

    <h1>🎓 AI Learning Buddy</h1>

    <p>
    Your Personal AI Tutor for Learning Python Basics
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="feature-container">

    <div class="feature-box">

    <h3>📖 Learn</h3>

    <p>
    Understand Python concepts with simple explanations and examples.
    </p>

    </div>


    <div class="feature-box">

    <h3>💡 Explore</h3>

    <p>
    Connect programming concepts with real-world applications.
    </p>

    </div>


    <div class="feature-box">

    <h3>📝 Practice</h3>

    <p>
    Test your knowledge with AI-generated quizzes and feedback.
    </p>

    </div>

    </div>
    """, unsafe_allow_html=True)


    st.divider()


    st.markdown("""
    <div class="section-card">

    <h2>🤖 Meet PyBuddy</h2>

    <p>
    PyBuddy is an AI-powered learning assistant designed
    to help beginners learn Python in an easy and interactive way.
    </p>

    <ul>

    <li>✅ Simple explanations</li>

    <li>✅ Real-life examples</li>

    <li>✅ Quiz generation</li>

    <li>✅ Personalized feedback</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)
# -----------------------------------
# LEARN PAGE
# -----------------------------------
elif page == "📖 Learn":

    st.title("📖 Learn Python Basics")

    topic = st.text_input(
        "Enter a Python topic",
        placeholder="Example: Variables"
    )

    if st.button("Explain"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:

            prompt = f"""
You are PyBuddy, a friendly AI Learning Buddy.

Your personality:
- Friendly
- Patient
- Encouraging
- Beginner-friendly
- Explain step by step
- Use simple English
- Give one real-life example
- End with one learning tip

Teach the following Python topic:

{topic}
"""



            with st.spinner("PyBuddy is teaching..."):

                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )

            st.success("Lesson Generated")

            st.write(response.text)

# -----------------------------------
# QUIZ PAGE
# -----------------------------------
elif page == "📝 Quiz":

    st.title("📝 Python Quiz Generator")

    quiz_topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Loops"
    )

    if st.button("Generate Quiz"):

        if quiz_topic.strip() == "":
            st.warning("Enter a topic.")
        else:

            prompt = f"""
You are PyBuddy, a friendly AI Learning Buddy.

Generate 5 beginner-friendly quiz questions on:

{quiz_topic}

Requirements:
- Keep questions simple.
- After the questions, provide the correct answers.
- Encourage the learner at the end.
"""

            with st.spinner("Generating Quiz..."):

                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )

            st.success("Quiz Ready")

            st.write(response.text)

# -----------------------------------
# FEEDBACK PAGE
# -----------------------------------
elif page == "✅ Feedback":

    st.title("✅ AI Feedback")

    topic = st.text_input(
        "Topic",
        placeholder="Example: Variables"
    )

    answer = st.text_area(
        "Write your answer here"
    )

    if st.button("Evaluate Answer"):

        if topic.strip() == "" or answer.strip() == "":
            st.warning("Please enter both the topic and your answer.")

        else:

            prompt = f"""
You are PyBuddy, a friendly AI Learning Buddy.

Evaluate the student's answer in a positive and encouraging way.

Topic:
{topic}

Student Answer:
{answer}

Provide:
1. Score out of 10
2. Strengths
3. Areas for improvement
4. Correct explanation
5. One motivational tip
"""

            with st.spinner("Evaluating..."):

                try:

                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt
                    )

                    st.success("Feedback Generated")

                    st.markdown(response.text)

                except Exception as e:

                    st.error("Gemini AI connection failed.")
                    st.write(e)

# -----------------------------------
# ABOUT
# -----------------------------------
else:

    st.title("ℹ About")

    st.write("""
### AI Learning Buddy

Developed using:

- Python
- Streamlit
- Google Gemini AI

Topic:

Python Basics

Prepared for the Infosys Springboard AI Learning Buddy Project.
""")

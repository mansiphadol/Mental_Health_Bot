import streamlit as st

# Streamlit app
st.title("UNISPECTRA BOT")
st.sidebar.title("Chat History")

# Initialize chat history
chat_history = []

# Function to update and display chat history


def update_chat_history(user_input, bot_response, sentiment_label):
    chat_history.append({
        'user': {'text': user_input, 'sentiment': sentiment_label},
        'bot': {'text': bot_response, 'sentiment': sentiment_label}
    })
    st.sidebar.text(f"User ({sentiment_label}): {user_input}")
    st.sidebar.text(f"Bot ({sentiment_label}): {bot_response}")

# Function to calculate depression score


def calculate_depression_score(user_responses):
    # Initialize a counter for "yes" answers
    yes_count = user_responses.count("Yes")

    # Calculate depression score based on the number of "yes" answers
    depression_score = yes_count * 20

    return f"Based on your responses, your depression score is {depression_score}%. I'm here to support you. If you need professional help, consider reaching out to a mental health professional."


# Streamlit input and output components
st.write("Welcome to UNISPECTRA Bot! Let's talk about your mental health.")
st.write("Please answer the following questions with 'Yes' or 'No'.")

questions = [
    "Have you ever experienced a terrible occurrence that has impacted you significantly? Examples may include being the victim of armed assault, witnessing a tragedy happen to someone else, surviving a sexual assault, or living through a natural disaster.",
    "Do you ever feel that you’ve been affected by feelings of edginess, anxiety, or nerves?",
    "Have you experienced a week or longer of lower-than-usual interest in activities that you usually enjoy? Examples might include work, exercise, or hobbies.",
    "Have you ever experienced an ‘attack’ of fear, anxiety, or panic?",
    "Do feelings of anxiety or discomfort around others bother you?"
]

user_responses = []

for i, question in enumerate(questions):
    response = st.radio(f"Question {i + 1}: {question}", ("Yes", "No"))
    user_responses.append(response)

if st.button("Submit"):
    # Calculate depression score
    depression_response = calculate_depression_score(user_responses)

    # Display depression response
    st.text(depression_response)

# "Delete Chat" button
if st.button("Delete Chat"):
    chat_history = []
    st.sidebar.text("Chat history deleted.")

# Display chat history in the sidebar
st.sidebar.title("Chat History")
for entry in chat_history:
    st.sidebar.text(
        f"User ({entry['user']['sentiment']}): {entry['user']['text']}")
    st.sidebar.text(
        f"Bot ({entry['bot']['sentiment']}): {entry['bot']['text']}")

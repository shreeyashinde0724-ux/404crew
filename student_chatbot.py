import random

# AIML Academic Syllabus – subject wise
aiml_syllabus = {
    "python": """🐍 Python Programming:
- Basics: Variables, Data types, Operators, Control structures
- Functions & Modules
- File handling
- Object-Oriented Programming (OOP)
- Exception Handling
- Libraries: NumPy, Pandas, Matplotlib""",

    "maths": """📐 Mathematics for AIML:
- Linear Algebra: Matrices, Vectors, Eigenvalues
- Probability & Statistics: Random variables, Distributions, Hypothesis testing
- Calculus: Differentiation, Integration, Optimization
- Discrete Mathematics: Logic, Graphs, Sets""",

    "ml": """🤖 Machine Learning:
- Supervised Learning: Regression, Classification
- Unsupervised Learning: Clustering, Dimensionality Reduction
- Model Evaluation: Accuracy, Precision, Recall, F1 Score
- Overfitting & Regularization
- ML Libraries: scikit-learn""",

    "ai": """🧠 Artificial Intelligence:
- Introduction to AI
- Search Algorithms (BFS, DFS, A*)
- Game Playing
- Knowledge Representation
- Expert Systems
- Applications of AI""",

    "dl": """🔮 Deep Learning:
- Neural Networks Basics: Perceptron, Activation functions
- Feedforward & Backpropagation
- CNNs (Convolutional Neural Networks)
- RNNs (Recurrent Neural Networks)
- Autoencoders & GANs
- Frameworks: TensorFlow, PyTorch""",

    "nlp": """🗣️ Natural Language Processing:
- Text preprocessing: Tokenization, Stemming, Lemmatization
- Bag of Words & TF-IDF
- Word Embeddings: Word2Vec, GloVe
- Sequence Models: RNN, LSTM
- Transformers & BERT
- Applications: Chatbots, Sentiment Analysis""",

    "ds": """📊 Data Science & Big Data:
- Data Collection & Cleaning
- Data Visualization
- Exploratory Data Analysis (EDA)
- Big Data Technologies: Hadoop, Spark
- Cloud platforms for AI/ML""",

    "capstone": """🎓 Capstone Project:
- End-to-end project applying AI/ML concepts
- Data preprocessing
- Model training & evaluation
- Deployment of AI solution"""
}

# General academic FAQs
academic_info = {
    "exam": "📅 The next exam is scheduled for 15th December 2025.",
    "syllabus": "📘 The full AIML syllabus includes Python, Maths, ML, AI, DL, NLP, DS, and a Capstone Project.",
    "library": "📚 The library is open from 9 AM to 6 PM, Monday to Saturday.",
    "contact": "☎️ You can reach the college office at +91-9876543210 or email: info@college.edu"
}

# Motivational quotes
quotes = [
    "🚀 Believe in yourself, you are capable of amazing things!",
    "🌟 Every expert was once a beginner.",
    "💡 Consistency is more important than motivation.",
    "🔥 Don’t stop when you’re tired. Stop when you’re done."
]

print("🤖 AIML Academic Assistant Chatbot")
print("Type 'exit' to quit.\n")

# Ask user's name
user_name = input("Chatbot: Hi! What’s your name? 😊\nYou: ").strip().capitalize()
if not user_name:
    user_name = "Student"

print(f"\nChatbot: Welcome {user_name}! I can help you with the AIML academic syllabus and college info. 🎓")
print("Chatbot: You can ask about subjects (Python, Maths, ML, AI, DL, NLP, DS, Capstone) or general queries like exam, syllabus, library, contact.\n")

while True:
    query = input(f"{user_name}: ").lower().strip()

    if query == "exit":
        print(f"Chatbot: Goodbye {user_name}! Keep learning and coding! 🎓")
        break

    # Greetings
    if any(greet in query for greet in ["hi", "hello", "hey"]):
        print(f"Chatbot: Hello {user_name}! Which subject or academic detail do you want to know about? 📘")

    # Polite replies
    elif "thank" in query or "thanks" in query:
        print("Chatbot: You're welcome! 😊 Keep studying hard!")
    elif "good morning" in query:
        print(f"Chatbot: Good morning, {user_name}! 🌞 Have a productive day ahead.")
    elif "good night" in query:
        print(f"Chatbot: Good night, {user_name}! 🌙 Don’t forget to dream big.")
    elif "bye" in query or "goodbye" in query:
        print(f"Chatbot: Bye {user_name}! 👋 Come back anytime to learn more.")
    elif "how are you" in query or "how r you" in query:
        print("Chatbot: I’m just a bot, but I’m happy to help you! 🤖 How are you?")

    # Motivational quotes
    elif "quote" in query or "motivate" in query:
        print("Chatbot:", random.choice(quotes))

    # Check general academic info
    elif any(key in query for key in academic_info):
        for key in academic_info:
            if key in query:
                print("Chatbot:", academic_info[key])
                break

    # Check syllabus
    else:
        found = False
        for subject in aiml_syllabus:
            if subject in query:
                print("\nChatbot:", aiml_syllabus[subject], "\n")
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I don't know that yet. Try asking about Python, Maths, ML, AI, DL, NLP, DS, Capstone, or general queries like exam, syllabus, library, contact.")

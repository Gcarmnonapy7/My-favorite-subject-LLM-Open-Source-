My Favorite Subject

My Favorite Subject is an open-source educational assistant powered by a custom-built Large Language Model (LLM). The project's mission is to help students better understand academic subjects by generating summaries and questions from input text in a simple and personal way.
🎓 Key Features

    Summarizes educational content provided by the user

    Designed to include a configurable assistant “persona”

    Lightweight backend API for connecting with any frontend

    Fully open-source and beginner-friendly for contributors

⚙️ Technologies Used

    Python 3.10+

    Flask (for backend API)

    Custom-built LLM (from scratch using PyTorch)

    HTML/CSS/JavaScript or React (for the frontend interface)

    🔧 Note: The history and persona system will be added in future versions.

⚡ Quick Start

# Clone the repository
git clone https://github.com/your-username/my-favorite-subject.git
cd my-favorite-subject

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Then open the frontend manually via frontend/index.html or connect a React frontend to the backend.
🧠 How It Works

    The user sends some input text (e.g., a lesson or topic).

    The backend runs it through the custom LLM.

    A summary and five questions (2 easy, 2 medium, 1 hard) are generated.

    The assistant returns the response without storing any history for now.

📦 To-Do (Coming Soon)

Add persona customization

Implement chat history system

Save user sessions

Image generator 

    Support voice interaction

✍️ Contributing

    Fork this repo

    Create a branch: git checkout -b feature-branch

    Make your changes

    Commit and push: git commit -m "Feature description"

    Open a Pull Request

📚 License

This project is licensed under the MIT License. Feel free to use and modify it!
🌱 Ideal For

    Students who want an AI study buddy

    Developers learning to build LLMs

    Open-source collaborators

    Anyone curious about AI in education

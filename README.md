#  🚀 AI Code Review Tool
An AI-powered web application to review and analyze code for errors, performance issues, and provide suggestions using AI.

#  🧑‍💻 Features
Code Analysis: Analyze Python code for errors and warnings.

AI Feedback: Get AI-generated suggestions using Hugging Face.

Code Explanation: AI explains the code in a simple, easy-to-understand way.

User-Friendly Interface: Simple and clean design for easy code input and feedback viewing.

#  🛠️ Tech Stack
Frontend: HTML, CSS

Backend: Python, Flask

AI Integration: Hugging Face API (StarCoder Model)

Linting: Pylint for static code analysis

#  🚀 Installation
Follow these steps to set up the project:

Clone the Repository

```bash
git clone https://github.com/AaronDeepak-B/AI-Code-Review-Tool.git
cd AI-Code-Review-Tool
Create and Activate Virtual Environment (Optional)
```
```bash
python -m venv env
source env/bin/activate    # On Linux/Mac
env\Scripts\activate       # On Windows
Install Dependencies
 ```

```bash
pip install -r requirements.txt
Set Up Hugging Face API Key

Replace "Bearer YOUR_API_KEY" in the code with your own API key from Hugging Face.
```

Run the Application

```bash
python a.py
The app will be available at http://127.0.0.1:5000.
```

#  🧪 Usage
Open your browser and go to http://127.0.0.1:5000.

Paste your Python code into the provided text area.

Click the "Analyze" button.

View the AI feedback, code explanations, and static analysis results.

#  🛡️ Troubleshooting
If you face ModuleNotFoundError, install missing dependencies using:

```bash
pip install -r requirements.txt
For Hugging Face API errors, ensure your API key is correct.***
```

If Flask errors occur, try restarting the server:

```bash
python a.py
```

#  📜 License
This project is licensed under the MIT License.

#  🌟 Contributing
Contributions are welcome!

Fork the repository.

Create a new branch: git checkout -b feature-branch

Commit your changes: git commit -m "Add your message"

Push to the branch: git push origin feature-branch

Open a Pull Request.

#  💬 Feedback
If you have any feedback, suggestions, or issues, feel free to open an issue in the GitHub repository.

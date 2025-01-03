# Stoic Sage Chatbot

Stoic Sage is a chatbot built with Django that delivers Stoic philosophy-based responses to user prompts. This project provides wisdom from Stoic philosophers like Marcus Aurelius, Epictetus, and Seneca to help users gain perspective and insight.

---

## Features

- **Keyword-Based Matching**: Matches user prompts with relevant Stoic quotes based on keywords, excluding words like "what," "why," "when," "where," "who," "how," and phrases like "I am," to focus on meaningful connections.
- **Fallback Quotes**: If no suitable quote is found, the chatbot provides a fallback response with a well-known Stoic quote.
- **Customizable**: Easily extendable to add more quotes, philosophers, or additional NLP features.

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Django 3.0+**
- **SQLite3** (default database, can be changed)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dust-Shadow/Stoic_Sage_Chatbot.git
   cd Stoic_Sage_Chatbot

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Setup Database:

bash
Copy code
python manage.py migrate
Load Initial Quotes Data: Ensure to load the initial data of Stoic quotes if available or add it manually in the Django Admin panel.

Run Server:

bash
Copy code
python manage.py runserver
Access the Chatbot: Open a browser and go to http://127.0.0.1:8000 to interact with Stoic Sage.

Project Structure
chat/: Contains the core chatbot application, including models, views, and utility functions.
chat/templates/chat/: Contains HTML files for the front end of the chatbot.
static/: Stores static files like CSS and JavaScript.
db.sqlite3: Default SQLite database.
manage.py: Django management script.

Usage
User Interaction: Enter phrases, and Stoic Sage responds with quotes from Stoic philosophers. For general inquiries or simple greetings (e.g., "Hello", "Hi"), it replies with, "Greetings, how may I serve you today?".
Keyword Filtering: Keywords like "what," "why," "where," "who," "I am," and "we are" are excluded from matching to better focus on relevant parts of the query.

Example Usage
Prompt: "Tell me about resilience."
Response:
Quote: "The impediment to action advances action. What stands in the way becomes the way."
Philosopher: Marcus Aurelius
Explanation: This quote highlights the Stoic belief in using obstacles as opportunities for growth and resilience.
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Fork the repo.
Create a new branch for your feature.
Make your changes and commit them.
Push your branch and create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries, please reach out to neerajhmakwana1357@gmail.com

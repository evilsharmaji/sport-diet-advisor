
# 🏋️‍♂️ Sport Diet Advisor – AI-Powered ChatBot

An intelligent, interactive **AI chatbot** built with **Streamlit** and **OpenRouter API**, designed to provide **personalized sports nutrition guidance** based on user-specific fitness goals, activity level, dietary needs, and training schedule.

---

## 🚀 Project Overview

**Sport Diet Advisor** revolutionizes how athletes receive nutritional guidance. Using AI and real-time interaction, this chatbot provides:
- Tailored meal plans
- Pre/post-workout nutrition
- Supplement advice
- Hydration strategies
- Evidence-based performance support

✨ Ideal for:
- Weight loss, muscle gain, endurance training
- Beginners to advanced-level athletes
- Users with dietary restrictions (e.g. vegan, gluten-free)

---

## 🧠 Features

- 🥗 **Personalized Nutrition**: Based on fitness level, goal, restrictions
- 💬 **Interactive Chatbot**: Ask real questions, get AI-powered responses
- 🧃 **Hydration & Recovery Advice**: Includes nutrient timing and tips
- 📊 **Markdown Tables**: AI outputs are cleanly structured and easy to follow
- 🔐 **Secure API Access**: API keys handled safely via `secrets.toml`

---


## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/evilsharmaji/sport-diet-advisor.git
cd sport-diet-advisor
```

### 2. Install Required Libraries

```bash
pip install streamlit requests pandas
```

### 3. Setup API Key in `.streamlit/secrets.toml`

Create a file: `.streamlit/secrets.toml`

```toml
[secrets]
API_KEY = "your_openrouter_api_key_here"
```

✅ This keeps your key secure and **out of your source code**.

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create a new app and connect your GitHub repo
4. Set the `API_KEY` in **Settings > Secrets** like this:

```toml
API_KEY = "your_openrouter_api_key_here"
```

5. Click **Deploy**

You will get a live app link like:

```
https://evilsharmaji-sport-diet-advisor.streamlit.app/
```

---

## 🧠 How It Works

1. Users select their fitness goal, experience level, and dietary restrictions
2. AI analyzes user context and gives:
   - Custom meal plans
   - Workout timing nutrition
   - Supplement advice
3. Built-in table formatting and emojis enhance readability
4. OpenRouter API powers the GPT-style AI engine

---

## 📚 Presentation Summary

- 70% of athletes fail to follow optimal diets (NSCA study)
- This AI tool generates real-time, adaptive, science-backed nutrition plans
- Integrates user data like body type, activity, preferences, and goals
- Includes hydration and supplement suggestions for peak performance
- Matches or exceeds traditional dieticians in accessibility and scale

---

## 🤖 Technologies Used

- [Streamlit](https://streamlit.io/) – UI & Web App
- [OpenRouter API](https://openrouter.ai/) – AI chat responses
- Python, Requests, Pandas

---

## 👨‍💻 Author

**Priyanshu Sharma**  
B.Tech CSE | AI Enthusiast    
GitHub: [@yourusername](https://github.com/evilsharmaji)

---

## 📜 License

This project is licensed under the MIT License.

---

## 💬 Want to contribute?

Feel free to open Issues or Pull Requests!

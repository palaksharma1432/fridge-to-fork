# 🍽️ Fridge2Fork — What's in Your Fridge? Recipe Randomizer

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Spoonacular API](https://img.shields.io/badge/Spoonacular-API-green)](https://spoonacular.com/food-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Turn your leftover ingredients into delicious meals!**  
> Input what's in your fridge, filter by dietary needs, and discover recipes — then save your favorites and auto-generate a shopping list for what's missing.

---

## 📸 Screenshots

> _Add screenshots of your app here after deployment._

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Getting a Spoonacular API Key](#getting-a-spoonacular-api-key)
- [Running the App](#-running-the-app)
- [Pushing to GitHub](#-pushing-to-github)
- [Deploying on Streamlit Cloud](#-deploying-on-streamlit-cloud)
- [Environment Variables](#-environment-variables)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🥦 **Ingredient Input** | Multi-select from common ingredients or type your own custom ones |
| 🥗 **Dietary Filters** | Filter recipes by Vegetarian, Vegan, or Gluten-Free |
| 🃏 **Recipe Cards** | Visual cards with recipe image, title, and missing ingredient count |
| 📖 **Detailed View** | Full recipe instructions, ingredients list, and cook time |
| ❤️ **Save Favorites** | Save and unsave recipes — stored locally as JSON |
| 🛒 **Shopping List** | Auto-generate a shopping list for ingredients you're missing |
| ⚡ **Clean UI** | Beginner-friendly, responsive Streamlit interface |

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) — Python-based web UI framework
- **Recipe Data:** [Spoonacular API](https://spoonacular.com/food-api) — Free tier (150 req/day)
- **Language:** Python 3.9+
- **Storage:** Local JSON file for saved favorites
- **Config:** `.env` file for API key management

---

## 📁 Project Structure

```
fridge2fork/
├── app.py                  # 🏠 Main Streamlit app — entry point
├── requirements.txt        # 📦 Python dependencies
├── .env                    # 🔑 API key (never commit this to GitHub!)
├── .gitignore              # 🚫 Files to exclude from Git
├── README.md               # 📖 You're reading this!
│
├── utils/
│   ├── api_handler.py      # 🌐 Spoonacular API calls
│   ├── database.py         # 💾 Favorites read/write logic
│   └── shopping_list.py    # 🛒 Shopping list generator
│
└── data/
    └── favorites.json      # ❤️ Saved recipes (auto-created on first save)
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- **Python 3.9+** → [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** → [Download here](https://git-scm.com/)
- A free **Spoonacular API key** (see below)

Check your Python version:
```bash
python --version
```

---

### Installation

**Step 1: Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/fridge2fork.git
cd fridge2fork
```

**Step 2: Create and activate a virtual environment** _(recommended)_
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Set up your `.env` file**
```bash
# Create the .env file
touch .env   # macOS/Linux
# or on Windows: type nul > .env
```

Open `.env` and add your API key:
```env
SPOONACULAR_API_KEY=your_api_key_here
```

**Step 5: Create the data folder**
```bash
mkdir data
```
> The `favorites.json` file will be created automatically when you first save a recipe.

---

### Getting a Spoonacular API Key

1. Go to [https://spoonacular.com/food-api](https://spoonacular.com/food-api)
2. Click **"Start for Free"** and create an account
3. After signing in, navigate to your **Profile → API Console**
4. Copy your **API Key**
5. Paste it into your `.env` file as shown above

> **Free Tier Limits:** 150 requests/day, 1 request/second. This is plenty for personal use!

---

## ▶️ Running the App

With your virtual environment active, run:

```bash
streamlit run app.py
```

Your browser will automatically open at `http://localhost:8501`.

To stop the app, press `Ctrl + C` in the terminal.

---

## 📤 Pushing to GitHub

**Step 1: Create a new repository on GitHub**

1. Go to [https://github.com/new](https://github.com/new)
2. Name it `fridge2fork`
3. Leave it **Public** (required for free Streamlit Cloud deployment)
4. Do **NOT** initialize with a README (you already have one)
5. Click **"Create repository"**

**Step 2: Make sure your `.gitignore` is set up**

Your `.gitignore` should contain at least:
```gitignore
.env
venv/
__pycache__/
*.pyc
.DS_Store
```
> ⚠️ **Never commit your `.env` file** — it contains your API key!

**Step 3: Initialize Git and push**
```bash
git init
git add .
git commit -m "🍽️ Initial commit — Fridge2Fork app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fridge2fork.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## ☁️ Deploying on Streamlit Cloud

Deploy your app for **free** at [https://streamlit.io/cloud](https://streamlit.io/cloud).

**Step 1:** Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub

**Step 2:** Click **"New app"**

**Step 3:** Fill in the details:
- **Repository:** `YOUR_USERNAME/fridge2fork`
- **Branch:** `main`
- **Main file path:** `app.py`

**Step 4:** Add your API key as a Secret
- Click **"Advanced settings"**
- Under **Secrets**, add:
```toml
SPOONACULAR_API_KEY = "your_api_key_here"
```

**Step 5:** Click **"Deploy!"**

Your app will be live at:
```
https://YOUR_USERNAME-fridge2fork-app-XXXX.streamlit.app
```

> 💡 **Why Secrets?** On Streamlit Cloud, you can't use a `.env` file. Secrets are the secure equivalent — your app reads them the same way via `os.getenv()`.

---

## 🔐 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `SPOONACULAR_API_KEY` | Your Spoonacular API key | ✅ Yes |

---

## ⚙️ How It Works

```
User inputs ingredients
        ↓
app.py collects inputs + filters
        ↓
api_handler.py → Spoonacular API
        ↓
Recipe cards displayed in Streamlit
        ↓
User clicks recipe → detailed view
        ↓
Save to favorites? → database.py → favorites.json
        ↓
Generate shopping list? → shopping_list.py → missing ingredients
```

### Key Files Explained

**`app.py`** — The main app. Handles the Streamlit UI, user inputs, and connects all the utility modules together.

**`utils/api_handler.py`** — Makes calls to the Spoonacular API to search for recipes by ingredients, fetch recipe details, and handle errors gracefully.

**`utils/database.py`** — Reads and writes to `data/favorites.json`. Handles saving, unsaving, and listing favorite recipes.

**`utils/shopping_list.py`** — Takes a recipe's full ingredient list and the user's current ingredients, then outputs a clean list of what still needs to be bought.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/my-new-feature`
3. **Commit** your changes: `git commit -m "Add my new feature"`
4. **Push** to the branch: `git push origin feature/my-new-feature`
5. **Open a Pull Request**

### Ideas for Contributions
- Add cuisine type filters (Italian, Asian, Mexican, etc.)
- Add calorie/nutrition display on recipe cards
- Export shopping list as a PDF or CSV
- Add a meal planner / weekly plan feature
- Support for multiple users with cloud storage

---

## 🐛 Troubleshooting

**App won't start?**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

**No recipes showing up?**
- Double-check your API key in `.env`
- You may have hit the free tier daily limit (150 requests/day)
- Try fewer or more common ingredients

**Favorites not saving?**
- Make sure the `data/` folder exists in your project root
- Check that you have write permissions in the directory

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Spoonacular](https://spoonacular.com/) for the fantastic food API
- [Streamlit](https://streamlit.io/) for making Python web apps so easy
- Everyone who contributed recipes and feedback ❤️

---

<div align="center">

Made with ❤️ and leftovers 🧅🥕🍳

**[⭐ Star this repo](https://github.com/YOUR_USERNAME/fridge2fork)** if you found it helpful!

</div>

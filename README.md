# 🍳 What's in Your Fridge? - Recipe Randomizer

A smart web application that helps you discover recipes based on ingredients you already have at home. Never wonder "what's for dinner?" again!

![App Screenshot](https://via.placeholder.com/800x400.png?text=App+Screenshot+Placeholder)

## ✨ Features

- **Ingredient-Based Search**: Input ingredients you have (multi-select + custom text)
- **Dietary Filters**: Filter recipes by vegetarian, vegan, and gluten-free preferences
- **Recipe Cards**: Beautiful cards showing recipe images and missing ingredients count
- **Detailed Recipe View**: Full recipes with cooking instructions
- **Favorites System**: Save and manage your favorite recipes
- **Shopping List**: Generate shopping lists from selected recipes
- **Clean Interface**: User-friendly design for seamless experience

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Spoonacular API key (free tier)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/fridge2fork.git
   cd fridge2fork

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
  ```bash
  pip install -r requirements.txt

4. **Set up your API key**

    - Get a free API key from Spoonacular
    - Create a .env file in the root directory
    - Add your API key:
    ```env
    SPOONACULAR_API_KEY=your_api_key_here

5. **Run the app**

  ```bash
  streamlit run app.py

6. Open your browser and navigate to http://localhost:8501

7. **Project Structure**

  fridge2fork/
  ├── app.py                 # Main Streamlit application
  ├── requirements.txt       # Python dependencies
  ├── .env                   # Environment variables (API key)
  ├── .gitignore            # Git ignore file
  ├── README.md             # Project documentation
  ├── utils/
  │   ├── __init__.py
  │   ├── api_handler.py    # Spoonacular API calls
  │   ├── database.py       # Favorites storage (JSON)
  │   └── shopping_list.py  # Shopping list generation
  └── data/
      └── favorites.json    # Saved recipes (auto-created)

## 🛠️ Technologies Used
Python 3.8+: Core programming language

Streamlit: Web application framework

Spoonacular API: Recipe database

JSON: Local data storage

python-dotenv: Environment variable management

## 📦 Dependencies
Create a requirements.txt file with:

```txt
streamlit==1.28.1
requests==2.31.0
python-dotenv==1.0.0
Pillow==10.0.1

## 🎯 How to Use
1. Enter Ingredients: Type ingredients you have in your fridge

2. Apply Filters: Select dietary preferences if needed

3. Get Recipes: Click "Find Recipes" to see suggestions

4. Explore: Browse recipe cards and click "View Recipe" for details

5. Save Favorites: ❤️ Save recipes you love

6. Shopping List: Add multiple recipes to generate a combined shopping list

## 🔧 Configuration
**Getting a Spoonacular API Key**
1. Visit Spoonacular API

2. Sign up for a free account

3. Navigate to your profile to get your API key

4. Copy the key to your .env file

**Free Tier Limits**
- 150 points/day (each recipe search costs ~1-3 points)

- Perfect for personal use and testing

## 🚢 Deployment on Streamlit Cloud
**1. Push code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/fridge2fork.git
git push -u origin main

**2. Deploy on Streamlit Cloud**

- Go to share.streamlit.io

- Sign in with GitHub

- Click "New app"

- Select your repository

- Add your Spoonacular API key in Streamlit Cloud secrets:

 -- Go to app settings → Secrets

 -- Add:

  ```toml
  SPOONACULAR_API_KEY = "your_api_key"

  Deploy!

## 🤝 Contributing
**Contributions are welcome! Feel free to:**

- Report bugs

- Suggest new features

- Submit pull requests

## 📝 License
This project is open source and available under the MIT License.

## ⚠️ Note
This app uses the free tier of Spoonacular API which has daily limits. For production use, consider upgrading to a paid plan.

## 🙏 Acknowledgments
- Spoonacular for the amazing recipe API

- Streamlit for the awesome framework

- All contributors and users of this app

**Happy Cooking! 🍳👨‍🍳**

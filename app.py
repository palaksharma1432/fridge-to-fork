import streamlit as st
from utils.api_handler import search_recipes, get_recipe_details
from utils.database import load_favorites, save_favorite, remove_favorite
from utils.shopping_list import generate_shopping_list

# Page Config
st.set_page_config(page_title="Fridge2Fork", page_icon="🍳", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .recipe-card { border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 20px; background-color: #f9f9f9; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar: Inputs & Filters
st.sidebar.title("🍱 My Fridge")
common_ingredients = ["Chicken", "Beef", "Pasta", "Tomato", "Eggs", "Milk", "Cheese", "Spinach", "Onion", "Garlic"]
selected_ingredients = st.sidebar.multiselect("Common items:", common_ingredients)
custom_ingredients = st.sidebar.text_input("Other items (comma separated):")

diet_filter = st.sidebar.selectbox("Dietary Preference:", [None, "Vegetarian", "Vegan", "Gluten Free"])

# Combine all ingredients
all_ingredients = selected_ingredients + ([i.strip() for i in custom_ingredients.split(",")] if custom_ingredients else [])

# App Navigation
tab1, tab2, tab3 = st.tabs(["🔍 Find Recipes", "⭐ Favorites", "🛒 Shopping List"])

with tab1:
    st.title("What should we cook today?")
    if st.button("Search Recipes") and all_ingredients:
        with st.spinner("Looking for recipes..."):
            results = search_recipes(all_ingredients, diet=diet_filter)
            st.session_state['results'] = results
    
    if 'results' in st.session_state:
        cols = st.columns(2)
        for i, recipe in enumerate(st.session_state['results']):
            with cols[i % 2]:
                st.image(recipe['image'], use_container_width=True)
                st.subheader(recipe['title'])
                st.write(f"❌ Missing: {recipe['missedIngredientCount']} ingredients")
                
                # Buttons
                c1, c2 = st.columns(2)
                if c1.button(f"View Details", key=f"view_{recipe['id']}"):
                    st.session_state['selected_recipe'] = recipe['id']
                
                if any(f['id'] == recipe['id'] for f in load_favorites()):
                    if c2.button("❤️ Saved", key=f"unsave_{recipe['id']}"):
                        remove_favorite(recipe['id'])
                        st.rerun()
                else:
                    if c2.button("🤍 Save", key=f"save_{recipe['id']}"):
                        save_favorite(recipe)
                        st.rerun()

    # Detailed View Popup (Simulation)
    if 'selected_recipe' in st.session_state:
        details = get_recipe_details(st.session_state['selected_recipe'])
        with st.expander("📖 Full Recipe View", expanded=True):
            st.header(details['title'])
            st.write(f"⏱️ Ready in: {details['readyInMinutes']} mins | 👥 Serves: {details['servings']}")
            st.write("### Instructions")
            st.write(details.get('instructions', "No instructions provided."))
            if st.button("Close Details"):
                del st.session_state['selected_recipe']
                st.rerun()

with tab2:
    st.header("Your Saved Recipes")
    favs = load_favorites()
    if not favs:
        st.info("You haven't saved any recipes yet.")
    else:
        for f in favs:
            st.write(f"- **{f['title']}**")
            if st.button("Remove", key=f"rem_{f['id']}"):
                remove_favorite(f['id'])
                st.rerun()

with tab3:
    st.header("Grocery List")
    favs = load_favorites()
    if favs:
        items = generate_shopping_list(favs)
        for item in items:
            st.checkbox(item)
        if st.button("Clear Favorites"):
            open("data/favorites.json", "w").write("[]")
            st.rerun()
    else:
        st.write("Save some recipes to generate a list!")
import streamlit as st

st.set_page_config(page_title="Emotion-Aware Diet Recommendation", page_icon="🥗", layout="centered")

st.title("🥗 Emotion-Aware Diet Recommendation System")
st.markdown("""
Welcome! This app recommends meals based on your **emotions**, **health goals**, and **cuisine preference**.
Stay healthy and happy! 🌟
""")

def detect_emotion(text):
    text = text.lower()
    if "sad" in text:
        return "Sad"
    elif "happy" in text:
        return "Happy"
    elif "angry" in text:
        return "Angry"
    elif "anxious" in text or "worried" in text:
        return "Anxious"
    else:
        return "Neutral"

nutrition_info_indian = {
    "Poha": {"Calories": 250, "Protein": 5, "Carbs": 50, "Fats": 6},
    "Paneer tikka": {"Calories": 280, "Protein": 15, "Carbs": 10, "Fats": 18},
    "Dal chawal": {"Calories": 350, "Protein": 12, "Carbs": 60, "Fats": 8},
}

nutrition_info_western = {
    "Dark chocolate": {"Calories": 170, "Protein": 2, "Carbs": 19, "Fats": 12},
    "Nuts": {"Calories": 180, "Protein": 6, "Carbs": 6, "Fats": 16},
    "Warm soup": {"Calories": 100, "Protein": 4, "Carbs": 15, "Fats": 2},
}

st.header("💬 Tell us how you feel today")
user_input = st.text_input("Describe your mood (e.g., I feel happy, sad, anxious...)")

st.header("🎯 Choose your health goal")
goal = st.selectbox("Select your goal:", ["Weight loss", "Muscle gain", "Maintenance", "Improve energy", "Improve mood"])

st.header("🍽️ Choose your cuisine")
cuisine = st.selectbox("Preferred cuisine:", ["Indian", "Western"])

placeholder = st.empty()

if st.button("Get Recommendations"):
    emotion = detect_emotion(user_input)
    
    if cuisine == "Indian":
        meals = ["Poha", "Paneer tikka", "Dal chawal"]
        nutrition = nutrition_info_indian
    else:
        meals = ["Dark chocolate", "Nuts", "Warm soup"]
        nutrition = nutrition_info_western

    goal_addition = {
        "Weight loss": "(low-calorie focus)",
        "Muscle gain": "(high-protein focus)",
        "Maintenance": "(balanced)",
        "Improve energy": "(extra carbs for energy)",
        "Improve mood": "(mood-boosting ingredients)"
    }

    meals = [meal + f" {goal_addition[goal]}" for meal in meals]

    with placeholder.container():
        st.success("Your personalized recommendations are ready! 🎉")
        st.subheader("✨ Summary")
        st.write(f"**Emotion detected:** {emotion}")
        st.write(f"**Goal:** {goal}")
        st.write(f"**Cuisine preference:** {cuisine}")

        st.header("🍲 Recommended Meals")
        for meal in meals:
            base_meal = meal.split(" (")[0]
            st.write(f"• {meal}")

            if base_meal in nutrition:
                info = nutrition[base_meal]
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Calories", f"{info['Calories']} kcal")
                    st.metric("Protein", f"{info['Protein']} g")
                with col2:
                    st.metric("Carbs", f"{info['Carbs']} g")
                    st.metric("Fats", f"{info['Fats']} g")

        st.image("https://source.unsplash.com/800x400/?healthy-food", caption="Eat well, feel better! 💚")

st.markdown("---")


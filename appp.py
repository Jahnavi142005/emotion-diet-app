import streamlit as st

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
    "Upma": {"Calories": 220, "Protein": 6, "Carbs": 45, "Fats": 5},
    "Dal chawal": {"Calories": 350, "Protein": 12, "Carbs": 60, "Fats": 8},
    "Roti sabzi": {"Calories": 300, "Protein": 8, "Carbs": 55, "Fats": 7},
    "Vegetable biryani": {"Calories": 400, "Protein": 8, "Carbs": 70, "Fats": 10},
    "Paneer tikka": {"Calories": 280, "Protein": 15, "Carbs": 10, "Fats": 18},
    "Idli sambhar": {"Calories": 280, "Protein": 10, "Carbs": 55, "Fats": 4},
    "Dhokla": {"Calories": 150, "Protein": 6, "Carbs": 25, "Fats": 4},
    "Rajma chawal": {"Calories": 420, "Protein": 14, "Carbs": 75, "Fats": 8},
    "Masala oats": {"Calories": 200, "Protein": 7, "Carbs": 35, "Fats": 5},
}

nutrition_info_western = {
    "Dark chocolate": {"Calories": 170, "Protein": 2, "Carbs": 19, "Fats": 12},
    "Nuts": {"Calories": 180, "Protein": 6, "Carbs": 6, "Fats": 16},
    "Warm soup": {"Calories": 100, "Protein": 4, "Carbs": 15, "Fats": 2},
    "Salad with fruits": {"Calories": 120, "Protein": 3, "Carbs": 20, "Fats": 4},
    "Smoothie bowl": {"Calories": 250, "Protein": 5, "Carbs": 40, "Fats": 6},
    "Balanced thali": {"Calories": 500, "Protein": 15, "Carbs": 60, "Fats": 15},
    "Vegetable stir fry": {"Calories": 200, "Protein": 6, "Carbs": 25, "Fats": 8},
}

def recommend_meals(emotion, goal, cuisine):
    if cuisine == "Indian":
        meals = ["Poha", "Paneer tikka", "Dal chawal"]
        nutrition = nutrition_info_indian
    else:
        meals = ["Dark chocolate", "Nuts", "Warm soup"]
        nutrition = nutrition_info_western

    if goal == "Weight loss":
        meals = [meal + " (low-calorie focus)" for meal in meals]
    elif goal == "Muscle gain":
        meals = [meal + " (high-protein focus)" for meal in meals]
    elif goal == "Improve energy":
        meals = [meal + " (extra carbs for energy)" for meal in meals]
    elif goal == "Improve mood":
        meals = [meal + " (mood-boosting ingredients)" for meal in meals]
    elif goal == "Maintenance":
        meals = [meal + " (balanced)" for meal in meals]

    return meals, nutrition

st.title("Emotion-Aware Diet Recommendation System")

user_input = st.text_input("How are you feeling today?")

goal = st.selectbox(
    "What is your health or dietary goal?",
    ["Weight loss", "Muscle gain", "Maintenance", "Improve energy", "Improve mood"]
)

cuisine = st.selectbox(
    "Which cuisine do you prefer?",
    ["Indian", "Western"]
)

placeholder = st.empty()

if st.button("Get Recommendations"):
    with placeholder.container():
        emotion = detect_emotion(user_input)
        st.write("## Your Personalized Recommendations")
        st.write(f"Detected Emotion: **{emotion}**")
        st.write(f"Selected Goal: **{goal}**")
        st.write(f"Cuisine Preference: **{cuisine}**")

        recommended_meals, nutrition = recommend_meals(emotion, goal, cuisine)
        st.write("### Recommended Meals for You:")

        for meal in recommended_meals:
            base_meal = meal.split(" (")[0]
            st.write(f"• {meal}")

            if base_meal in nutrition:
                info = nutrition[base_meal]
                st.write(f"  Calories: {info['Calories']} kcal")
                st.write(f"  Protein: {info['Protein']} g")
                st.write(f"  Carbs: {info['Carbs']} g")
                st.write(f"  Fats: {info['Fats']} g")

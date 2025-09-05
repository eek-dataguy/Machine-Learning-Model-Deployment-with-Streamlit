import streamlit as st

appetizers_list = [
        "Spring Rolls",
        "Stuffed Mushrooms",
        "Bruschetta",
        "Chicken Satay",
        "Mini Quiches"
    ]

main_courses = [
    "Grilled Salmon with Lemon Butter",
    "Beef Lok Lak",
    "Chicken Alfredo Pasta",
    "Vegetable Stir Fry with Tofu",
    "Roast Duck with Tamarind Sauce",
    "Spaghetti Bolognese",
    "Khmer Amok Fish",
    "Lamb Curry with Jasmine Rice",
    "Stuffed Bell Peppers",
    "BBQ Pork Ribs"
    ]

desserts = [
    "Mango Sticky Rice",
    "Pumpkin Custard",
    "Chocolate Lava Cake",
    "Coconut Ice Cream",
    "Banana Fritters",
    "Tiramisu",
    "Fruit Tart",
    "Creme Brulee",
    "Khmer Jelly Dessert (Chè)",
    "Pandan Cake",
    "Rice Pudding",
    "Cheesecake",
    "Mocha Mousse",
    "Lemon Sorbet",
    "Caramel Flan"
    ]

with st.form("form_key"):
    st.write("What whould you like to order?")
    
    appetizer = st.selectbox("Appetizers", options=appetizers_list)
    main = st.selectbox("Main Courses", options=main_courses)
    dess = st.selectbox("Desserts", options=desserts)

    wine = st.checkbox("Are you bringing wine?")

    visit_date = st.date_input("When are you coming?")
    visit_time = st.time_input("At What time are you coming?")

    allergies = st.text_area("Any allergies?", placeholder="Leave us any note about your allergies!")

    submit_btn = st.form_submit_button("Submit")



st.write(f"""
***
         Your order summary:
         - Appitizer        : {appetizer},
         - Main Course      : {main},
         - Desserts         : {dess},
         - Bring wine       : {"Yes" if wine else "No" }
         - Schedule         : {visit_date} : {visit_time}
         - Allergies Notes  : {allergies}

***
""")
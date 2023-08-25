import streamlit as st

# Dictionary of available raw materials
available_raw_materials = {
    'egg': 4,
    'flour': 2,
    'milk': 1,
    'sugar': 3,
    'butter': 2,
    'cocoa powder': 1
}

# Dictionary of dishes and their required raw materials
dishes = {
    'Pancakes': {'egg': 1, 'flour': 1, 'milk': 1, 'butter': 1},
    'Chocolate Cake': {'egg': 2, 'flour': 1, 'sugar': 1, 'butter': 1, 'cocoa powder': 1},
    'Vanilla Cupcakes': {'egg': 2, 'flour': 1, 'sugar': 1, 'butter': 1, 'milk': 1}
}


def suggest_dishes(available_raw_materials):
    suggested_dishes = []
    for dish, ingredients in dishes.items():
        if all(ingredient in available_raw_materials and available_raw_materials[ingredient] >= quantity for ingredient, quantity in ingredients.items()):
            suggested_dishes.append(dish)
    return suggested_dishes

# Streamlit app


def main():
    st.title("Dish Suggestion App")

    st.sidebar.title("Available Raw Materials")
    for ingredient, quantity in available_raw_materials.items():
        available_raw_materials[ingredient] = st.sidebar.number_input(
            ingredient, value=quantity, min_value=0)

    suggested_dishes = suggest_dishes(available_raw_materials)

    st.subheader("Available Raw Materials:")
    for ingredient, quantity in available_raw_materials.items():
        st.write(f"- {ingredient}: {quantity}")

    st.subheader("Suggested Dishes:")
    if suggested_dishes:
        for dish in suggested_dishes:
            st.write(f"- {dish}")
    else:
        st.write("No dishes can be made with the available raw materials.")


if __name__ == '__main__':
    main()

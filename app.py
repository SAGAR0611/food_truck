import streamlit as st
from datetime import datetime
import time
import random

# --- Database / Menu Setup ---
# A dictionary to simulate a database for menu items.
# Structure: {location: {time_of_day: {item_name: {details}}}}
MENU = {
    "Business District": {
        "Morning": {
            "Espresso": {"price": 3.50, "desc": "A strong shot of coffee to kickstart your day.", "img": "https://images.unsplash.com/photo-1593443320739-77f6497c759f?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Breakfast Burrito": {"price": 8.00, "desc": "Packed with eggs, cheese, salsa, and your choice of bacon or avocado.", "img": "https://images.unsplash.com/photo-1627462318428-43b86beb479e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Pancakes": {"price": 7.50, "desc": "Fluffy pancakes served with maple syrup and fresh berries.", "img": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        },
        "Afternoon": {
            "Gourmet Sandwich": {"price": 10.50, "desc": "Artisan bread with premium deli meats, cheese, and fresh greens.", "img": "https://images.unsplash.com/photo-1528738337798-a62c623a8337?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Quinoa Salad": {"price": 9.00, "desc": "A healthy and refreshing mix of quinoa, vegetables, and lemon vinaigrette.", "img": "https://images.unsplash.com/photo-1551248429-42971d21e25b?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Iced Tea": {"price": 3.00, "desc": "Freshly brewed and chilled black tea with a hint of lemon.", "img": "https://images.unsplash.com/photo-1556745753-b2904692b3cd?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        },
        "Evening": {
            "Smash Burger": {"price": 12.00, "desc": "Two juicy beef patties smashed on the grill with cheese and special sauce.", "img": "https://images.unsplash.com/photo-1607013251379-e6eecfffe234?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Loaded Fries": {"price": 8.50, "desc": "Crispy fries topped with cheese, bacon bits, and sour cream.", "img": "https://images.unsplash.com/photo-1598679253447-a89b5a5b54e3?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Craft Soda": {"price": 4.00, "desc": "Locally sourced craft soda with unique flavor profiles.", "img": "https://images.unsplash.com/photo-1624517452488-048692791668?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        }
    },
    "Residential Area": {
        "Morning": {
            "Drip Coffee": {"price": 2.50, "desc": "Classic, smooth, and reliable drip coffee.", "img": "https://images.unsplash.com/photo-1511920183353-3c9c9b0a7a49?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Oatmeal Bowl": {"price": 6.00, "desc": "Warm oatmeal with your choice of toppings like nuts, fruits, and honey.", "img": "https://images.unsplash.com/photo-1585237630263-35698b111186?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        },
        "Afternoon": {
            "Chicken Wrap": {"price": 9.50, "desc": "Grilled chicken, lettuce, tomato, and ranch dressing in a soft tortilla.", "img": "https://images.unsplash.com/photo-1629503576222-b95285e0d293?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Smoothie": {"price": 7.00, "desc": "A blend of fresh fruits, yogurt, and a touch of honey.", "img": "https://images.unsplash.com/photo-1502741224143-94386982b831?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        },
        "Evening": {
            "Margherita Pizza": {"price": 14.00, "desc": "Classic pizza with fresh mozzarella, basil, and tomato sauce.", "img": "https://images.unsplash.com/photo-1598021680133-eb3a171d872c?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
            "Garlic Knots": {"price": 5.00, "desc": "Warm, buttery garlic knots served with marinara sauce.", "img": "https://images.unsplash.com/photo-1627308595186-e711203c9b74?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=600"},
        }
    }
}

# --- Helper Functions ---

def get_time_of_day(hour):
    """Determines if it's Morning, Afternoon, or Evening."""
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    else:
        return "Evening"

def get_current_menu(location, time_of_day):
    """Retrieves the correct menu based on location and time."""
    # Add evening menu items to the afternoon menu in the business district
    if location == "Business District" and time_of_day == "Afternoon":
        combined_menu = MENU[location]["Afternoon"].copy()
        combined_menu.update(MENU[location]["Evening"])
        return combined_menu
    return MENU.get(location, {}).get(time_of_day, {})

# --- Streamlit App ---

st.set_page_config(page_title="Gemini's Gourmet Food Truck", layout="wide")

# --- Session State Initialization ---
# This is crucial for keeping track of the cart across reruns.
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- Sidebar for Simulation Controls & Cart ---

with st.sidebar:
    st.title("🚚 Truck Controls")
    st.write("Simulate the truck's status.")

    # Location-based menu control
    location = st.selectbox(
        "📍 Truck Location",
        ("Business District", "Residential Area")
    )

    # Time-based menu control
    current_hour = st.slider(
        "🕒 Time of Day (Hour)", 0, 23, datetime.now().hour
    )
    time_of_day = get_time_of_day(current_hour)

    # Online/Offline status control
    is_online = st.toggle("✅ Truck Online", value=True)
    
    st.divider()

    # --- Shopping Cart UI ---
    st.title("🛒 Your Cart")
    
    if not st.session_state.cart:
        st.write("Your cart is empty.")
    else:
        total_price = 0
        for item, details in st.session_state.cart.items():
            price = details['price'] * details['quantity']
            total_price += price
            st.write(f"- {details['quantity']}x {item}: ${price:.2f}")

        st.divider()
        st.metric(label="Total Price", value=f"${total_price:.2f}")
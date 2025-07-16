Objective:



Create an interactive application using Python and Streamlit that allows customers to place food orders from a moving food truck. The menu will vary based on time and location, and the app will allow both online and offline ordering options. The app should also allow customers to select quantities for their orders.

Key Features to Implement:

User Interface (UI):

Design a clean and intuitive UI for customers to easily view and select from the menu.

Display a dynamic menu that changes based on time of day (morning, afternoon, evening) or location (food truck’s current position).

Show food options with images, descriptions, and prices.

Order Functionality:

Order Process: Customers should be able to:

Select an item from the menu.

Specify the quantity of the item.

Add the item to their cart.

Review their order before final submission.

Location-based Menu Adjustment:

The app should track the location of the food truck and update the menu accordingly based on the truck's movement. For example, the menu might offer different items based on whether the truck is in a residential area or a business district.

Time-based Menu Adjustment:

The menu should adjust according to the time of day. For instance:

Morning: Breakfast items (coffee, pancakes, etc.).

Afternoon: Lunch items (sandwiches, wraps, salads, etc.).

Evening: Dinner options (burgers, pizzas, etc.).

Online and Offline Ordering:

Online: Allow customers to place orders when the truck is parked and online.

Offline: When the truck is moving or temporarily offline, customers should still be able to browse the menu, but orders can’t be placed until the truck goes online again.

Cart and Checkout:

The cart should display all selected items with their quantities and total price.

Include an option to edit or remove items before checkout.

Provide a “Place Order” button that finalizes the purchase.

Implement order confirmation with an estimated delivery/pickup time.

Backend and Database:

Store menu items, prices, and inventory in a database (e.g., SQLite or a simple in-memory solution for simplicity).

Track customer orders and quantities, including any special instructions.

Technical Requirements:

Frontend: Streamlit will be used for building the app interface. Streamlit's interactive features will allow the customer to interact with the menu, make orders, and review selections.

Backend: Use Python to manage the app’s logic, such as adjusting the menu based on time and location, handling orders, and updating inventory.

Location Handling: Integrate a simple GPS or location feature to track where the food truck is, using a mock location for development.

Optional Features (for Further Enhancement):

Implement a payment gateway for online orders.

Add a customer login feature for order history.

Integrate a review/rating system for the food truck experience.
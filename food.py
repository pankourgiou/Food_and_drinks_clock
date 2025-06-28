import tkinter as tk
import time
from datetime import datetime

# Food/Drinks for each hour
menu_clock = {
    0: "Midnight Snack: Hot chocolate & cookies 🍪",
    1: "Late Night Treat: Cheese toast & herbal tea 🧀🍵",
    2: "Sleepy Hour: Warm milk & banana 🍌",
    3: "Dream Snack: Almonds & chamomile tea 🌙",
    4: "Early Bite: Greek yogurt & honey 🍯",
    5: "Sunrise Sips: Fresh orange juice & croissant 🥐🍊",
    6: "Breakfast: Eggs, toast, and coffee ☕🍳",
    7: "Morning Boost: espresso  & oatmeal 🥣",
    8: "Second Breakfast: Pancakes & maple syrup 🥞",
    9: "Brunch Time: Avocado toast & cappuccino 🥑☕",
    10: "Late Morning Craving: Muffin & latte 🧁",
    11: "Pre-Lunch: Fruit salad & iced tea 🍓🍑",
    12: "Lunch: Pasta & lemonade 🍝🍋",
    13: "Lunch Add-on: Caesar salad & sparkling water 🥗",
    14: "Sweet Hour: Ice cream & espresso 🍨",
    15: "Tea Time: Biscuits & earl grey tea 🍪🍵",
    16: "Afternoon Pick-Me-Up: Sandwich & iced coffee 🥪",
    17: "Pre-Dinner Snack: Nachos & soda 🧃",
    18: "Dinner: Grilled chicken & red wine 🍷🍗",
    19: "Dinner Treat: Sushi & green tea 🍣🍵",
    20: "Evening Relax: Soup & bread 🥖",
    21: "Dessert Hour: Chocolate mousse & liqueur 🍫",
    22: "Chill Snack: Popcorn & milkshake 🍿🥤",
    23: "Wind Down: Tea & dark chocolate 🍫"
}

# GUI Colors and Fonts
bg_color = "#fffaf0"
text_color = "#4b3621"
font_main = ("Helvetica", 36, "bold")
font_small = ("Helvetica", 18)

# Create GUI window
root = tk.Tk()
root.title("Food & Drinks Clock")
root.geometry("600x300")
root.configure(bg=bg_color)

# Time and Menu Labels
time_label = tk.Label(root, font=font_main, bg=bg_color, fg=text_color)
time_label.pack(pady=30)

menu_label = tk.Label(root, font=font_small, bg=bg_color, fg=text_color, wraplength=500)
menu_label.pack()

# Update Clock and Menu
def update_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = now.hour
    menu = menu_clock[hour]

    time_label.config(text=current_time)
    menu_label.config(text=f"🍴 {menu}")
    root.after(1000, update_clock)

update_clock()
root.mainloop()

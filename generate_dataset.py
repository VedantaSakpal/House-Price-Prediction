import pandas as pd
import random
import os

random.seed(42)

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

locations = ["Mumbai", "Pune", "Thane", "Navi Mumbai", "Kalyan"]

data = []

for i in range(1000):
    area = random.randint(600, 4000)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    age = random.randint(0, 30)
    parking = random.randint(0, 2)
    location = random.choice(locations)

    # Base price
    price = (
        area * 8000
        + bedrooms * 500000
        + bathrooms * 300000
        + parking * 200000
        - age * 50000
    )

    # Location effect
    if location == "Mumbai":
        price += 5000000
    elif location == "Pune":
        price += 2500000
    elif location == "Thane":
        price += 1800000
    elif location == "Navi Mumbai":
        price += 2200000
    else:
        price += 1200000

    data.append([
        area,
        bedrooms,
        bathrooms,
        age,
        parking,
        location,
        price
    ])

df = pd.DataFrame(data, columns=[
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Age",
    "Parking",
    "Location",
    "Price"
])

df.to_csv("data/house_data.csv", index=False)

print("✅ Dataset created successfully!")
print(f"Total rows: {len(df)}")
print(df.head())
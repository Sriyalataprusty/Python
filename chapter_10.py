# Comprehension
car_brand = ['BMW', 'Maruti', 'Mercedes', 'Tata', 'Maruti'] 
# List comprehension
m_brand = [brand for brand in car_brand if "m" in brand.lower()]
sm_brand = [brand for brand in car_brand if brand.lower().startswith("m")]
# print(m_brand)

# Set comprehension
a_brand = {brand for brand in car_brand if "m" in brand.lower()}
# print(a_brand)

# Dictonary Comprehension
car_price = {
    "BMW": 45_30_000,
    "Maruti": 3_50_000,
    "Mercedes": 44_46_000,
    "Tata": 4_57_000
}
costly_brand = {brand: starting_price for brand, starting_price in car_price.items() if starting_price > 40_00_000}
# print(costly_brand)

car ={
    "BMW": {'2 series gram coupe': 45_30_000, 
            'iX1': 49_90_000,
            '3 series gram series limousine': 60_45_000, 
            'X3': 71_20_00, 
            '5 series': 72_35_000 },
    
    "Maruti": {'s_presso': 3_50_000,
               'alto K10': 3_70_000,
               'wagana':4_99_000,
               'swift': 5_79_000,
               'jimny': 12_31_000},
    
    "Mercedes": {'Benz A Class Limousine': 44_43_000, 
                 'Benz C Class': 58_65_000,
                 'Benz E Class':78_50_000,
                 'Benz S Class': 1_78_00_000,
                 'Maybach s_Class':2_74_50_000 },
    
    "Tata": {'Tiago': 4_57_000, 
             'Punch': 5_50_000, 
             'Safari': 14_66_000,
             'Herier': 25_25_250,
             'Herier EV': 30_30_303}
}

brand_name = {f"{brand} {model} starts at {price}" for brand, models in car.items() for model,price in models.items() if price > 40_00_000}
print(brand_name)

def pitching_car(brand_name):
    for car in brand_name: print(car, "\n")

pitching_car(brand_name)

brand_name = {}

for brand, models in car.items(): 
    for model, price in models.items():
        if price > 40_00_000:
            brand_name.add(f"{brand} {model} starts at {price}.")
        
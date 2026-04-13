import pandas as pd

weather_stations = [
    {"station_id": 10, "city": "Oradea", "temp_c": 23.8, "wind_kmh": 12, "is_coastal": False},
    {"station_id": 20, "city": "Bucharest", "temp_c": 26.4, "wind_kmh": 14, "is_coastal": False },
    {"station_id": 30, "city": "Moscow", "temp_c": 18.2, "wind_kmh": 18, "is_coastal": False },
    {"station_id": 40, "city": "San Diego", "temp_c": 28.9, "wind_kmh": 22, "is_coastal": True },
    {"station_id": 50, "city": "Lisbon", "temp_c": 32.4, "wind_kmh": 25, "is_coastal": True },
    {"station_id": 60, "city": "Budapest", "temp_c": 27.4, "wind_kmh": 13, "is_coastal": False }
]

cities = []
temps = []
winds = []
is_coastal = []
ids = []
for record in weather_stations:
    ids.append(record["station_id"])
    cities.append(record["city"])
    temps.append(record["temp_c"])
    winds.append(record["wind_kmh"])
    is_coastal.append(record["is_coastal"])
my_1st_df = pd.DataFrame(weather_stations, index=ids)





second_wheater_stations = {
    "station_id" : ids,
    "city": cities,
    "temp_c": temps,
    "wind_kmh": winds,
    "is_coastal": is_coastal
} 
my_2nd_df = pd.DataFrame(second_wheater_stations, index= ids)

print(my_1st_df)
print(my_2nd_df)

def station_report(label, df):
    print(f"{label}")
    print("-shape:")
    print(df.shape)
    print("\n-head:")
    print(df.head(2))
    print("\n-tail:")
    print(df.tail(1))
    print(df.dtypes)

station_report("---First report---", my_1st_df)
station_report("\n---Second report---", my_2nd_df)
print("Shapes match:", my_1st_df.shape == my_2nd_df.shape)

temperatures = my_1st_df["temp_c"]
print("---Temperature Series---")
print(temperatures)
print(type(temperatures))

#Question: What would go wrong if `wind_kmh` contained a string like `'N/A'` in one row? How would `dtypes` help you catch that?
#'dtypes' would just modify the type to object

#If wind_kmh key is completely missing from the dict - we get key error when we want to append nothing to a list. 

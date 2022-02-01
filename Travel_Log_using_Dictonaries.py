travel_log_new_ = [
    {
        "country": "India",
        "cities_visited": ["Thiruvananthapuram", "Madras"],
        "Number_of_visits": 100
    },

    {
        "country": "Japan",
        "cities_visited": ["Tokyo", "Fukuoka"],
        "Number_of_visits": 100
    }
]


def add_travel_history(country, visits, cities):
    #new_country = {}
    # new_country["country"]=country
    # new_country["cities_visited"]=cities
    # new_country["Number_of_visits"]=visits
    # travel_log_new_.append(new_country)

    new_country = {"country": country, "cities_visited": cities, "Number_of_visits": visits}
    travel_log_new_.append(new_country)

add_travel_history(country="USA", visits=1, cities=["Denver", "San Fransisco"])

print(travel_log_new_)
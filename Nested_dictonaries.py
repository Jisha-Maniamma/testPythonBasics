a = ["a", "b", ["c", "d"]]

travel_log = {
    "India": ["Kerala", "TamilNadu"],
    "Japan": "Fukuoka"
}

# nesting a dictionary in a dictonary
travel_log_new = {
    "India": {
        "cities_visited": ["Thiruvananthapuram", "Madras"],
        "Number_of_visits": 100
    },

    "Japan": {
        "cities_visited": ["Tokyo", "Fukuoka"],
        "Number_of_visits": 100
    }
}

# nesting dictonary in list
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

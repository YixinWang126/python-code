cities = {  
    'Tokyo': {  
        'country': 'Japan',  
        'population': '13.9 million',  
        'fact': 'Tokyo is the capital and most populous city in Japan.'  
    },  
    'New York': {  
        'country': 'United States',  
        'population': '8.6 million',  
        'fact': 'New York City is the most populous city in the United States.'  
    },  
    'London': {  
        'country': 'United Kingdom',  
        'population': '9.3 million',  
        'fact': 'London is the capital and most populous city of the United Kingdom.'  
    }  
}  

for city_name, city_info in cities.items():  
    print(f"City: {city_name}")  
    print(f"Country: {city_info['country']}")  
    print(f"Population: {city_info['population']}")  
    print(f"Fact: {city_info['fact']}")  
    print() 
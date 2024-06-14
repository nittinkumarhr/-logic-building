"""write a python program that takes an array of user objects. Each user object will have properties like `id`, `name`, `city`, and other relevant information. The component should render a list of users grouped by cities. Display the city name as a heading, and under each city, list the names of the users belonging to that city. For example, if the 
List is: const users = [   
{ id: 1, name: "nitin", city: "Bijnor" },   
{ id: 2, name: "mohit Smith", city: "Bijnor" },   
{ id: 3, name: "punit", city: "noida " },   
{ id: 4, name: "tushar", city: "dhampur" }, ];
[12:27 PM] Himanshu Kishore
Expected Output : 
Bijnor:
- nitin
- mohit
 
noida:
- punit
 
dhampur:
- tushar"""
def group_users_by_city(users):
    group = {}
    for user in users:
        city = user['city']
        if city not in group:
            group[city] = []
           
        group[city].append(user['name'])
        
        """{'Bijnor': ['nitin']}
            {'Bijnor': ['nitin', 'mohit ']}
            {'Bijnor': ['nitin', 'mohit '], 'noida ': ['punit']}
            {'Bijnor': ['nitin', 'mohit '], 'noida ': ['punit'], 'dhampur': ['tushar']}"""
    
    for all in group.items():
        # print(f"{city}:\n-{(str(city_users))}")
        print(all[0],":\n","\n ".join(all[1]))

# Example usage
users =  [   
{ id: 1, 'name': "nitin", 'city': "Bijnor" },   
{ id: 2, 'name': "mohit ", 'city': "Bijnor" },   
{ id: 3, 'name': "punit", 'city': "noida " },   
{ id: 4, 'name': "tushar", 'city': "dhampur" }, ]

group_users_by_city(users)

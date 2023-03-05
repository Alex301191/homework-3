import requests


def get_information_about_superheroes():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    superhero_list = response.json()
    return superhero_list


def get_intelligence_list(superhero_list, key_list):
    hero_intelligence = {}
    for key in key_list:
        for hero in superhero_list:
            if key in hero['biography']['fullName'] or key in hero['biography']['aliases']:
                hero_intelligence[key] = int(hero['powerstats']['intelligence'])
    return hero_intelligence


def find_the_smartest(hero_intelligence):
    the_smartest = max(hero_intelligence, key=hero_intelligence.get)
    return the_smartest


if __name__ == "__main__":
    key_list = ['Hulk', 'Captain America', 'Thanos']
    superhero_list = get_information_about_superheroes()
    hero_intelligence = get_intelligence_list(superhero_list, key_list)
    print(f'{find_the_smartest(hero_intelligence)} является самым умным')

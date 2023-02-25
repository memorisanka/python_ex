users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]


def find_people_from_poland(lst: list) -> list:
    return [user for user in lst if user.get("country") == "Poland"]


print(find_people_from_poland(users))

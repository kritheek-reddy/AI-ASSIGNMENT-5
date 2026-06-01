from knowledge_base import tourist_places, food_recommendations


def filter_places(city, interests, budget):
    selected_places = []

    for place in tourist_places:
        if place["city"].lower() != city.lower():
            continue

        if place["cost"] > budget:
            continue

        for interest in interests:
            if interest.lower() in place["best_for"] or interest.lower() == place["category"]:
                selected_places.append(place)
                break

    return selected_places


def create_day_plan(city, interests, budget, max_hours):
    places = filter_places(city, interests, budget)

    plan = []
    total_cost = 0
    total_time = 0

    for place in places:
        if total_cost + place["cost"] <= budget and total_time + place["time_hours"] <= max_hours:
            plan.append(place)
            total_cost += place["cost"]
            total_time += place["time_hours"]

    return plan, total_cost, total_time


def recommend_food(place):
    category = place["category"]

    if category in food_recommendations:
        return food_recommendations[category]

    return place["food"]


def display_plan(city, interests, budget, max_hours):
    plan, total_cost, total_time = create_day_plan(city, interests, budget, max_hours)

    print("AI Based Travel Planner")
    print("-----------------------")
    print("City:", city)
    print("Interests:", ", ".join(interests))
    print("Budget:", budget)
    print("Available Hours:", max_hours)
    print()

    if not plan:
        print("No suitable plan found for the given preferences.")
        return

    print("Recommended Travel Plan:")
    print()

    for index, place in enumerate(plan, start=1):
        print(index, ".", place["name"])
        print("   Category:", place["category"])
        print("   Approx Cost:", place["cost"])
        print("   Time Required:", place["time_hours"], "hours")
        print("   Recommended Food:", ", ".join(recommend_food(place)))
        print()

    print("Total Estimated Cost:", total_cost)
    print("Total Time Required:", total_time, "hours")


if __name__ == "__main__":
    city = "Hyderabad"
    interests = ["history", "culture", "photography"]
    budget = 1000
    max_hours = 8

    display_plan(city, interests, budget, max_hours)

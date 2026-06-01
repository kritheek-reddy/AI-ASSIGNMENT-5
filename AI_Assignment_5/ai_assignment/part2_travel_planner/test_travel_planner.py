from travel_planner import display_plan


print("Test Case 1: Heritage and Culture Trip")
display_plan(
    city="Hyderabad",
    interests=["history", "culture"],
    budget=1000,
    max_hours=8
)

print("\n" + "=" * 50 + "\n")

print("Test Case 2: Nature and Photography Trip")
display_plan(
    city="Hyderabad",
    interests=["nature", "photography"],
    budget=700,
    max_hours=5
)

print("\n" + "=" * 50 + "\n")

print("Test Case 3: Entertainment Trip")
display_plan(
    city="Hyderabad",
    interests=["entertainment", "family"],
    budget=2000,
    max_hours=8
)

from knowledge_graph import build_travel_knowledge_graph


kg = build_travel_knowledge_graph()

print("Test Case 1: Display all facts")
kg.display_facts()

print("\n" + "=" * 50 + "\n")

print("Test Case 2: Find facts where subject is Hyderabad")
results = kg.find_by_subject("Hyderabad")
for result in results:
    print(result)

print("\n" + "=" * 50 + "\n")

print("Test Case 3: Find all locatedIn relations")
results = kg.find_by_relation("locatedIn")
for result in results:
    print(result)

print("\n" + "=" * 50 + "\n")

print("Test Case 4: Find entities connected to Charminar")
results = kg.find_connected_entities("Charminar")
for result in results:
    print(result)

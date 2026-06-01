class KnowledgeGraph:
    def __init__(self):
        self.triples = []

    def add_fact(self, subject, relation, obj):
        self.triples.append((subject, relation, obj))

    def display_facts(self):
        print("Knowledge Graph Facts")
        print("---------------------")

        for subject, relation, obj in self.triples:
            print(subject, "--", relation, "-->", obj)

    def find_by_subject(self, subject):
        results = []

        for s, r, o in self.triples:
            if s.lower() == subject.lower():
                results.append((s, r, o))

        return results

    def find_by_relation(self, relation):
        results = []

        for s, r, o in self.triples:
            if r.lower() == relation.lower():
                results.append((s, r, o))

        return results

    def find_connected_entities(self, entity):
        results = []

        for s, r, o in self.triples:
            if s.lower() == entity.lower() or o.lower() == entity.lower():
                results.append((s, r, o))

        return results


def build_travel_knowledge_graph():
    kg = KnowledgeGraph()

    kg.add_fact("Hyderabad", "hasPlace", "Charminar")
    kg.add_fact("Hyderabad", "hasPlace", "Golconda Fort")
    kg.add_fact("Hyderabad", "hasPlace", "Salar Jung Museum")
    kg.add_fact("Hyderabad", "hasFood", "Biryani")
    kg.add_fact("Hyderabad", "hasFood", "Irani Chai")

    kg.add_fact("Charminar", "type", "Heritage Monument")
    kg.add_fact("Golconda Fort", "type", "Historical Fort")
    kg.add_fact("Salar Jung Museum", "type", "Museum")

    kg.add_fact("Charminar", "locatedIn", "Hyderabad")
    kg.add_fact("Golconda Fort", "locatedIn", "Hyderabad")
    kg.add_fact("Salar Jung Museum", "locatedIn", "Hyderabad")

    kg.add_fact("Biryani", "isFamousFoodOf", "Hyderabad")
    kg.add_fact("Irani Chai", "isFamousFoodOf", "Hyderabad")

    kg.add_fact("Charminar", "bestFor", "Photography")
    kg.add_fact("Golconda Fort", "bestFor", "History")
    kg.add_fact("Salar Jung Museum", "bestFor", "Art")

    return kg


if __name__ == "__main__":
    kg = build_travel_knowledge_graph()

    kg.display_facts()

    print("\nFacts about Hyderabad:")
    for fact in kg.find_by_subject("Hyderabad"):
        print(fact)

    print("\nPlaces located in Hyderabad:")
    for fact in kg.find_by_relation("locatedIn"):
        print(fact)

    print("\nEntities connected to Charminar:")
    for fact in kg.find_connected_entities("Charminar"):
        print(fact)

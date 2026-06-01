# Part 3: Knowledge Graphs

## Objective

The objective of this part is to describe Knowledge Graphs and explore the tools used to build Knowledge Graphs.

A simple Python-based Knowledge Graph is also implemented using subject-relation-object triples.

## What is a Knowledge Graph?

A Knowledge Graph is a structured representation of information where entities are connected through relationships.

In a Knowledge Graph:

- Entities are represented as nodes
- Relationships are represented as edges
- Facts are stored as triples

A triple has the form:

```text
Subject → Relation → Object
```

Example:

```text
Hyderabad → hasPlace → Charminar
Charminar → locatedIn → Hyderabad
Hyderabad → hasFood → Biryani
```

## Domain Chosen

The selected domain is tourism.

The Knowledge Graph represents information about:

- Cities
- Tourist places
- Famous food
- Place categories
- User interests
- Relationships between entities

## Files

```text
part3_knowledge_graphs/
│
├── knowledge_graph.py
├── test_knowledge_graph.py
├── output.txt
└── README.md
```

## File Description

### `knowledge_graph.py`

This file contains the main implementation of the Knowledge Graph.

It includes functions to:

- Add facts
- Display all facts
- Search facts by subject
- Search facts by relation
- Find connected entities

### `test_knowledge_graph.py`

This file contains test cases for checking the Knowledge Graph implementation.

### `output.txt`

This file contains the execution output of the test cases.

## Knowledge Representation

The Knowledge Graph stores facts as triples.

Each fact is stored in this format:

```python
(subject, relation, object)
```

Example:

```python
("Hyderabad", "hasPlace", "Charminar")
```

This means Hyderabad has a tourist place called Charminar.

## Example Facts Used

```text
Hyderabad -- hasPlace --> Charminar
Hyderabad -- hasPlace --> Golconda Fort
Hyderabad -- hasFood --> Biryani
Charminar -- locatedIn --> Hyderabad
Golconda Fort -- type --> Historical Fort
Salar Jung Museum -- type --> Museum
Biryani -- isFamousFoodOf --> Hyderabad
```

## Tools Used to Build Knowledge Graphs

Some common tools used for building Knowledge Graphs are:

### 1. Neo4j

Neo4j is a graph database used to store and query connected data.

It uses the Cypher query language.

Example:

```text
MATCH (city)-[:hasPlace]->(place)
RETURN city, place
```

### 2. RDF

RDF stands for Resource Description Framework.

It stores information in triples:

```text
Subject → Predicate → Object
```

### 3. Protégé

Protégé is an ontology editor used to create domain models and define relationships between concepts.

### 4. SPARQL

SPARQL is a query language used for RDF-based Knowledge Graphs.

It is used to retrieve and manipulate graph data.

### 5. NetworkX

NetworkX is a Python library used to create and analyze graphs.

It can be used for small Knowledge Graph experiments and graph visualization.

## Functions Implemented

### `add_fact(subject, relation, obj)`

Adds a new fact to the Knowledge Graph.

### `display_facts()`

Displays all facts stored in the graph.

### `find_by_subject(subject)`

Finds all triples where the given entity is the subject.

### `find_by_relation(relation)`

Finds all triples with the given relation.

### `find_connected_entities(entity)`

Finds all triples where the given entity appears either as subject or object.

## How to Run

Open Terminal inside the `part3_knowledge_graphs` folder.

Run the main file:

```bash
python3 knowledge_graph.py
```

Run the test cases:

```bash
python3 test_knowledge_graph.py
```

Save the output:

```bash
python3 test_knowledge_graph.py > output.txt
```

## Sample Output

```text
Knowledge Graph Facts
---------------------
Hyderabad -- hasPlace --> Charminar
Hyderabad -- hasPlace --> Golconda Fort
Hyderabad -- hasPlace --> Salar Jung Museum
Hyderabad -- hasFood --> Biryani
Hyderabad -- hasFood --> Irani Chai
Charminar -- type --> Heritage Monument
Golconda Fort -- type --> Historical Fort
```

## Conclusion

Knowledge Graphs are useful for representing connected information in a meaningful way.

They help AI systems understand relationships between different entities.

In this part, a simple tourism-based Knowledge Graph was implemented using Python triples.

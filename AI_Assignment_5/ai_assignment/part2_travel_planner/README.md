# Part 2: AI Based Travel Planner

## Objective

The objective of this assignment is to design an AI based Travel Planner that reuses an existing knowledge base in the travel domain.

The system recommends tourist places, food options, estimated cost, and a personalized tour plan based on user preferences.

## Domain Selected

The selected domain is **Tourism and Travel Planning**.

The planner uses a small knowledge base containing information about:

- Tourist places
- City
- Place category
- Approximate cost
- Time required
- Food recommendations
- User interests

## Features

The Travel Planner performs the following tasks:

1. Takes user preferences such as city, interests, budget, and available time.
2. Searches the knowledge base for suitable tourist places.
3. Filters places according to the user's budget.
4. Matches places with user interests.
5. Suggests food options based on the type of place.
6. Calculates total estimated cost.
7. Calculates total time required.
8. Displays a personalized travel plan.

## Folder Structure

```text
part2_travel_planner/
│
├── knowledge_base.py
├── travel_planner.py
├── test_travel_planner.py
├── output.txt
└── README.md
```

## File Description

### `knowledge_base.py`

This file contains the travel knowledge base.

Each place is stored with details such as:

- Name
- City
- Category
- Cost
- Time required
- Nearby food options
- Suitable interests

### `travel_planner.py`

This file contains the main logic of the AI based Travel Planner.

It includes functions for:

- Filtering places
- Creating a day plan
- Recommending food
- Displaying the final travel plan

### `test_travel_planner.py`

This file contains multiple test cases to check whether the planner works correctly for different user preferences.

### `output.txt`

This file stores the execution output of the test cases.

## Knowledge Base Representation

The knowledge base is represented using Python dictionaries and lists.

Example:

```python
{
    "name": "Charminar",
    "city": "Hyderabad",
    "category": "heritage",
    "cost": 200,
    "time_hours": 2,
    "food": ["Irani Chai", "Osmania Biscuits"],
    "best_for": ["history", "architecture", "photography"]
}
```

## Working of the System

The system works in the following steps:

1. The user gives input such as city, interests, budget, and available time.
2. The system checks each place in the knowledge base.
3. Places that do not match the city are ignored.
4. Places above the budget are ignored.
5. Places matching the user's interests are selected.
6. The selected places are added to the plan if they fit within the available time and budget.
7. Food recommendations are selected based on the place category.
8. The final plan is displayed with total cost and total time.

## Example Input

```text
City: Hyderabad
Interests: history, culture, photography
Budget: 1000
Available Hours: 8
```

## Example Output

```text
AI Based Travel Planner
-----------------------
City: Hyderabad
Interests: history, culture, photography
Budget: 1000
Available Hours: 8

Recommended Travel Plan:

1 . Charminar
   Category: heritage
   Approx Cost: 200
   Time Required: 2 hours
   Recommended Food: Hyderabadi Biryani, Irani Chai, Kebabs

2 . Golconda Fort
   Category: heritage
   Approx Cost: 300
   Time Required: 3 hours
   Recommended Food: Hyderabadi Biryani, Irani Chai, Kebabs

3 . Salar Jung Museum
   Category: museum
   Approx Cost: 150
   Time Required: 3 hours
   Recommended Food: South Indian Meals, Tea, Snacks

Total Estimated Cost: 650
Total Time Required: 8 hours
```

## Test Cases

The implementation is tested using three different travel preferences.

### Test Case 1: Heritage and Culture Trip

```text
City: Hyderabad
Interests: history, culture
Budget: 1000
Available Hours: 8
```

### Test Case 2: Nature and Photography Trip

```text
City: Hyderabad
Interests: nature, photography
Budget: 700
Available Hours: 5
```

### Test Case 3: Entertainment Trip

```text
City: Hyderabad
Interests: entertainment, family
Budget: 2000
Available Hours: 8
```

## How to Run

Open Terminal and go to the Part 2 folder:

```bash
cd ~/Desktop/AI_Assignments/ai_assignment/part2_travel_planner
```

Run the main file:

```bash
python3 travel_planner.py
```

Run the test cases:

```bash
python3 test_travel_planner.py
```

Save the execution output:

```bash
python3 test_travel_planner.py > output.txt
```

View the saved output:

```bash
cat output.txt
```

## Concepts Used

This assignment demonstrates the following AI concepts:

- Knowledge representation
- Rule based reasoning
- Recommendation system
- Cost assessment
- Personalized planning
- Use of domain knowledge base

## Conclusion

The AI based Travel Planner shows how a simple knowledge base can be reused to create personalized travel recommendations.

The system uses user preferences and basic rules to recommend places, food options, cost estimates, and a suitable tour plan.

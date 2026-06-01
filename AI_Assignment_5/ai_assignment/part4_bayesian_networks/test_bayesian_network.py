from bayesian_network import BayesianNetwork


network = BayesianNetwork()

test_cases = [
    {
        "name": "Test Case 1: Fever, Cough, and Fatigue present",
        "evidence": {
            "fever": True,
            "cough": True,
            "fatigue": True
        }
    },
    {
        "name": "Test Case 2: Fever and Cough present, Fatigue absent",
        "evidence": {
            "fever": True,
            "cough": True,
            "fatigue": False
        }
    },
    {
        "name": "Test Case 3: Only Fever present",
        "evidence": {
            "fever": True,
            "cough": False,
            "fatigue": False
        }
    },
    {
        "name": "Test Case 4: No symptoms present",
        "evidence": {
            "fever": False,
            "cough": False,
            "fatigue": False
        }
    }
]

print("Bayesian Network Test Cases")
print("===========================")

for test in test_cases:
    probability = network.calculate_flu_probability(test["evidence"])
    diagnosis = network.give_diagnosis(probability)

    print()
    print(test["name"])
    print("Evidence:", test["evidence"])
    print("Probability of Flu:", round(probability, 4))
    print("Diagnosis:", diagnosis)

# Part 4: Bayesian Network

## Objective

The objective of this part is to explore Bayesian Networks for representing uncertainty, modelling problems, and performing simple inference.

A Bayesian Network is a probabilistic graphical model that represents variables as nodes and dependencies as directed edges.

## Problem Selected

The selected example is a simple **medical diagnosis model**.

The model estimates whether a person may have flu based on symptoms such as fever, cough, and fatigue.

## Variables Used

The Bayesian Network uses the following variables:

- Flu
- Fever
- Cough
- Fatigue

## Network Structure

The structure of the Bayesian Network is:

```text
Flu → Fever
Flu → Cough
Flu → Fatigue
```

This means that having flu can influence the probability of having fever, cough, and fatigue.

## Files

```text
part4_bayesian_networks/
│
├── bayesian_network.py
├── test_bayesian_network.py
├── output.txt
└── README.md
```

## File Description

### `bayesian_network.py`

This file contains the implementation of the Bayesian Network.

It includes:

- Prior probability of flu
- Conditional probabilities of symptoms given flu
- Probability calculation
- Simple inference using Bayes' theorem

### `test_bayesian_network.py`

This file contains test cases for different symptom combinations.

### `output.txt`

This file contains the execution output of the test cases.

## Bayesian Network Explanation

A Bayesian Network represents probabilistic relationships between variables.

For this assignment, flu is treated as the main cause, and symptoms are treated as effects.

Example:

```text
P(Fever | Flu)
P(Cough | Flu)
P(Fatigue | Flu)
```

The system calculates:

```text
P(Flu | Evidence)
```

where evidence can be symptoms such as fever, cough, and fatigue.

## Probability Values Used

The following probabilities are used:

```text
P(Flu) = 0.10
P(No Flu) = 0.90

P(Fever | Flu) = 0.90
P(Fever | No Flu) = 0.20

P(Cough | Flu) = 0.80
P(Cough | No Flu) = 0.30

P(Fatigue | Flu) = 0.70
P(Fatigue | No Flu) = 0.25
```

## Inference Method

Bayes' theorem is used to calculate the probability of flu given symptoms.

The formula used is:

```text
P(Flu | Evidence) = P(Evidence | Flu) × P(Flu) / P(Evidence)
```

where:

```text
P(Evidence) = P(Evidence | Flu) × P(Flu) + P(Evidence | No Flu) × P(No Flu)
```

## How to Run

Open Terminal inside the folder and run:

```bash
python3 bayesian_network.py
```

To run the test cases:

```bash
python3 test_bayesian_network.py
```

To save output:

```bash
python3 test_bayesian_network.py > output.txt
```

## Sample Output

```text
Bayesian Network: Flu Diagnosis
--------------------------------
Evidence: fever=True, cough=True, fatigue=True
Probability of Flu: 0.8016
Diagnosis: High chance of flu
```

## Applications of Bayesian Networks

Bayesian Networks are used in:

- Medical diagnosis
- Risk prediction
- Spam filtering
- Fault detection
- Decision support systems
- Recommendation systems

## Conclusion

Bayesian Networks are useful for reasoning under uncertainty.

This implementation shows how symptoms can be used as evidence to estimate the probability of flu using Bayes' theorem.

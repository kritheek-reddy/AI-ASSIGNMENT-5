class BayesianNetwork:
    def __init__(self):
        self.prior_flu = 0.10
        self.prior_no_flu = 0.90

        self.symptom_probabilities = {
            "fever": {
                True: 0.90,
                False: 0.10,
                "no_flu_true": 0.20,
                "no_flu_false": 0.80
            },
            "cough": {
                True: 0.80,
                False: 0.20,
                "no_flu_true": 0.30,
                "no_flu_false": 0.70
            },
            "fatigue": {
                True: 0.70,
                False: 0.30,
                "no_flu_true": 0.25,
                "no_flu_false": 0.75
            }
        }

    def evidence_given_flu(self, evidence):
        probability = 1

        for symptom, value in evidence.items():
            probability *= self.symptom_probabilities[symptom][value]

        return probability

    def evidence_given_no_flu(self, evidence):
        probability = 1

        for symptom, value in evidence.items():
            if value is True:
                probability *= self.symptom_probabilities[symptom]["no_flu_true"]
            else:
                probability *= self.symptom_probabilities[symptom]["no_flu_false"]

        return probability

    def calculate_flu_probability(self, evidence):
        likelihood_flu = self.evidence_given_flu(evidence)
        likelihood_no_flu = self.evidence_given_no_flu(evidence)

        numerator = likelihood_flu * self.prior_flu

        denominator = (
            likelihood_flu * self.prior_flu
            + likelihood_no_flu * self.prior_no_flu
        )

        if denominator == 0:
            return 0

        return numerator / denominator

    def give_diagnosis(self, probability):
        if probability >= 0.70:
            return "High chance of flu"
        elif probability >= 0.40:
            return "Moderate chance of flu"
        else:
            return "Low chance of flu"


if __name__ == "__main__":
    network = BayesianNetwork()

    evidence = {
        "fever": True,
        "cough": True,
        "fatigue": True
    }

    probability = network.calculate_flu_probability(evidence)

    print("Bayesian Network: Flu Diagnosis")
    print("--------------------------------")
    print("Evidence: fever=True, cough=True, fatigue=True")
    print("Probability of Flu:", round(probability, 4))
    print("Diagnosis:", network.give_diagnosis(probability))

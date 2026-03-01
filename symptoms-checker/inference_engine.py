"""
Inference Engine for the Symptoms Checker Expert System.

Implements weighted forward-chaining:
  1. Accept a set of active symptoms (facts) from the user.
  2. For each rule in the knowledge base, compute a match score.
  3. Return all rules sorted by confidence (descending), filtered above a threshold.

Scoring formula
---------------
For a rule with N conditions:
  - Each condition that matches the current facts contributes (weight / N) points.
  - Conditions that explicitly require a symptom to be False and it is absent
    are counted as partial positive signals (they narrow down the diagnosis).
  - The raw score is normalised to a 0–100 confidence percentage.
"""

from dataclasses import dataclass
from typing import List

from knowledge_base import Rule, RULES


@dataclass
class DiagnosisResult:
    conclusion: str
    description: str
    advice: str
    confidence: float          # 0.0 – 100.0
    matched_conditions: int
    total_conditions: int


class InferenceEngine:
    def __init__(self, rules: List[Rule] = None, threshold: float = 30.0):
        self.rules = rules if rules is not None else RULES
        self.threshold = threshold   # minimum confidence % to include in results

    def evaluate(self, active_symptoms: set[str]) -> List[DiagnosisResult]:
        """
        Run forward chaining against the active symptom set.

        Parameters
        ----------
        active_symptoms : set[str]
            Names of symptoms the user has reported as present.

        Returns
        -------
        List[DiagnosisResult]
            Matching diagnoses sorted by confidence, highest first.
            Only results at or above self.threshold are returned.
        """
        results: List[DiagnosisResult] = []

        for rule in self.rules:
            matched = 0
            total = len(rule.conditions)

            for symptom, expected in rule.conditions.items():
                symptom_present = symptom in active_symptoms
                if expected is True and symptom_present:
                    matched += 1
                elif expected is False and not symptom_present:
                    matched += 1

            if total == 0:
                continue

            raw_score = (matched / total) * rule.weight
            max_score = rule.weight
            confidence = (raw_score / max_score) * 100.0

            if confidence >= self.threshold:
                results.append(
                    DiagnosisResult(
                        conclusion=rule.conclusion,
                        description=rule.description,
                        advice=rule.advice,
                        confidence=round(confidence, 1),
                        matched_conditions=matched,
                        total_conditions=total,
                    )
                )

        results.sort(key=lambda r: r.confidence, reverse=True)
        return results

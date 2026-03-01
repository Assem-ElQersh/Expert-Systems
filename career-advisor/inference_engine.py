"""
Inference Engine for the Career Path Advisor Expert System.

Implements weighted forward-chaining for career recommendation:
  1. Accept the user's trait profile (dict of category → selected value).
  2. For each CareerRule, compute how many trait conditions match.
  3. Return all rules sorted by confidence (descending), filtered above a threshold.

Scoring formula
---------------
For a rule with N conditions:
  - Each condition whose expected value matches the user's selection contributes
    (weight / N) points to the raw score.
  - Confidence is normalised to a 0–100 percentage:
      confidence = (matched / total) × 100
  - The weight influences ranking when two rules have the same match ratio.
"""

from dataclasses import dataclass
from typing import Dict, List

from knowledge_base import CareerRule, CAREER_RULES


@dataclass
class CareerRecommendation:
    career: str
    field: str
    description: str
    roadmap: str
    skills_to_develop: List[str]
    confidence: float          # 0.0 – 100.0
    matched_traits: int
    total_traits: int


class InferenceEngine:
    def __init__(self, rules: List[CareerRule] = None, threshold: float = 40.0):
        self.rules = rules if rules is not None else CAREER_RULES
        self.threshold = threshold

    def evaluate(self, user_profile: Dict[str, str]) -> List[CareerRecommendation]:
        """
        Run forward chaining against the user's trait profile.

        Parameters
        ----------
        user_profile : dict
            Mapping of trait category → selected value,
            e.g. {"Primary Interest": "Technology & Computing", ...}

        Returns
        -------
        List[CareerRecommendation]
            Matching careers sorted by confidence, highest first.
            Only results at or above self.threshold are returned.
        """
        results: List[CareerRecommendation] = []

        for rule in self.rules:
            matched = 0
            total = len(rule.conditions)

            for trait_category, expected_value in rule.conditions.items():
                user_value = user_profile.get(trait_category)
                if user_value == expected_value:
                    matched += 1

            if total == 0:
                continue

            confidence = (matched / total) * 100.0

            if confidence >= self.threshold:
                results.append(
                    CareerRecommendation(
                        career=rule.career,
                        field=rule.field,
                        description=rule.description,
                        roadmap=rule.roadmap,
                        skills_to_develop=rule.skills_to_develop,
                        confidence=round(confidence, 1),
                        matched_traits=matched,
                        total_traits=total,
                    )
                )

        results.sort(key=lambda r: (r.confidence, r.matched_traits), reverse=True)
        return results

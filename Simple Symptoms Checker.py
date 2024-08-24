import tkinter as tk
from tkinter import messagebox


class ExpertSystem:
    def __init__(self):
        self.knowledge_base = []
        self.inference_engine = InferenceEngine()

    def add_rule(self, rule):
        self.knowledge_base.append(rule)

    def diagnose(self, symptoms):
        return self.inference_engine.evaluate(self.knowledge_base, symptoms)

class Rule:
    def __init__(self, conditions, conclusion, weight=1):
        self.conditions = conditions
        self.conclusion = conclusion
        self.weight = weight

    def match_score(self, symptoms):
        score = 0
        total_weight = 0

        for symptom, expected in self.conditions.items():
            total_weight += self.weight
            if symptoms.get(symptom) == expected:
                score += self.weight

        return score / total_weight if total_weight > 0 else 0

class InferenceEngine:
    def evaluate(self, knowledge_base, symptoms):
        best_match = None
        highest_score = 0

        for rule in knowledge_base:
            score = rule.match_score(symptoms)
            if score > highest_score:
                highest_score = score
                best_match = rule

        if best_match:
            return best_match.conclusion
        return "No diagnosis could be made."

class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expert System - Simple Symptoms Checker")

        self.symptom_vars = {
            "fever": tk.BooleanVar(),
            "cough": tk.BooleanVar(),
            "fatigue": tk.BooleanVar(),
            "sneezing": tk.BooleanVar(),
            "runny nose": tk.BooleanVar(),
            "sore throat": tk.BooleanVar()
        }

        self.setup_ui()
        self.setup_expert_system()

    def setup_ui(self):
        tk.Label(self.root, text="Select your symptoms:").pack(anchor='w')

        for symptom, var in self.symptom_vars.items():
            tk.Checkbutton(self.root, text=symptom.capitalize(), variable=var).pack(anchor='w')

        tk.Button(self.root, text="Diagnose", command=self.diagnose).pack()

    def setup_expert_system(self):
        self.expert_system = ExpertSystem()
        rule1 = Rule({"fever": True, "cough": True, "fatigue": True}, "Flu", weight=3)
        rule2 = Rule({"sneezing": True, "runny nose": True, "sore throat": True}, "Cold", weight=2)
        rule3 = Rule({"fever": True, "fatigue": True, "sore throat": False}, "Likely Flu", weight=1)
        self.expert_system.add_rule(rule1)
        self.expert_system.add_rule(rule2)
        self.expert_system.add_rule(rule3)

    def diagnose(self):
        symptoms = {symptom: var.get() for symptom, var in self.symptom_vars.items()}
        diagnosis = self.expert_system.diagnose(symptoms)
        messagebox.showinfo("Diagnosis Result", f"Diagnosis: {diagnosis}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()

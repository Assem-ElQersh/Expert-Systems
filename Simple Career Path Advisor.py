import tkinter as tk
from tkinter import messagebox


class CareerPathExpertSystem:
    def __init__(self):
        self.knowledge_base = []
        self.inference_engine = InferenceEngine()

    def add_rule(self, rule):
        self.knowledge_base.append(rule)

    def suggest_career(self, profile):
        return self.inference_engine.evaluate(self.knowledge_base, profile)

class Rule:
    def __init__(self, conditions, career, roadmap, weight=1):
        self.conditions = conditions
        self.career = career
        self.roadmap = roadmap
        self.weight = weight

    def match_score(self, profile):
        score = 0
        total_weight = 0

        for trait, expected in self.conditions.items():
            total_weight += self.weight
            if profile.get(trait) == expected:
                score += self.weight

        return score / total_weight if total_weight > 0 else 0

class InferenceEngine:
    def evaluate(self, knowledge_base, profile):
        best_match = None
        highest_score = 0

        for rule in knowledge_base:
            score = rule.match_score(profile)
            if score > highest_score:
                highest_score = score
                best_match = rule

        if best_match:
            return f"Suggested Career: {best_match.career}\nRoadmap: {best_match.roadmap}"
        return "No suitable career path could be suggested."

class CareerAdvisorGUI:
    def __init__(self, root, expert_system):
        self.root = root
        self.root.title("CareerPathAdvisor: Comprehensive Career Guidance")
        self.expert_system = expert_system

        # Define GUI Elements
        self.interests_label = tk.Label(root, text="Select your Interest:")
        self.interests_label.grid(row=0, column=0)
        self.interests_var = tk.StringVar(value="technology")
        self.interests_dropdown = tk.OptionMenu(root, self.interests_var, "technology", "creativity", "social impact", "business", "science")
        self.interests_dropdown.grid(row=0, column=1)

        self.skills_label = tk.Label(root, text="Select your Key Skill:")
        self.skills_label.grid(row=1, column=0)
        self.skills_var = tk.StringVar(value="analytical")
        self.skills_dropdown = tk.OptionMenu(root, self.skills_var, "analytical", "communication", "leadership", "technical", "management")
        self.skills_dropdown.grid(row=1, column=1)

        self.values_label = tk.Label(root, text="Select your Core Value:")
        self.values_label.grid(row=2, column=0)
        self.values_var = tk.StringVar(value="innovation")
        self.values_dropdown = tk.OptionMenu(root, self.values_var, "innovation", "autonomy", "helping others", "stability", "challenge")
        self.values_dropdown.grid(row=2, column=1)

        self.personality_label = tk.Label(root, text="Select your Personality:")
        self.personality_label.grid(row=3, column=0)
        self.personality_var = tk.StringVar(value="logical")
        self.personality_dropdown = tk.OptionMenu(root, self.personality_var, "logical", "artistic", "empathetic", "strategic", "practical")
        self.personality_dropdown.grid(row=3, column=1)

        self.education_label = tk.Label(root, text="Select your Education Level:")
        self.education_label.grid(row=4, column=0)
        self.education_var = tk.StringVar(value="Computer Science")
        self.education_dropdown = tk.OptionMenu(root, self.education_var, "Computer Science", "Fine Arts", "Sociology", "Business", "Biology")
        self.education_dropdown.grid(row=4, column=1)

        self.submit_button = tk.Button(root, text="Get Career Suggestion", command=self.get_suggestion)
        self.submit_button.grid(row=5, column=0, columnspan=2)

    def get_suggestion(self):
        profile = {
            "interest": self.interests_var.get(),
            "skill": self.skills_var.get(),
            "value": self.values_var.get(),
            "personality": self.personality_var.get(),
            "education": self.education_var.get()
        }
        suggestion = self.expert_system.suggest_career(profile)
        messagebox.showinfo("Career Suggestion", suggestion)

# Define comprehensive career rules
rule1 = Rule(
    {"interest": "technology", "skill": "analytical", "value": "innovation", "personality": "logical", "education": "Computer Science"},
    "Data Science",
    "Earn a degree in Data Science, learn machine learning algorithms, build a portfolio, apply for data science roles.",
    weight=3
)
rule2 = Rule(
    {"interest": "creativity", "skill": "communication", "value": "autonomy", "personality": "artistic", "education": "Fine Arts"},
    "Graphic Design",
    "Earn a degree in Graphic Design, master design software, create a portfolio, freelance or join a design firm.",
    weight=3
)
rule3 = Rule(
    {"interest": "social impact", "skill": "leadership", "value": "helping others", "personality": "empathetic", "education": "Sociology"},
    "Non-Profit Management",
    "Earn a degree in Non-Profit Management, gain experience in leadership roles, network with other professionals in the field.",
    weight=3
)
rule4 = Rule(
    {"interest": "business", "skill": "management", "value": "stability", "personality": "strategic", "education": "Business"},
    "Business Management",
    "Earn a degree in Business Administration, develop leadership skills, gain experience in managerial roles, aim for executive positions.",
    weight=3
)
rule5 = Rule(
    {"interest": "science", "skill": "technical", "value": "challenge", "personality": "practical", "education": "Biology"},
    "Biotechnology",
    "Earn a degree in Biotechnology, gain laboratory experience, focus on innovation in the biotech industry, pursue research roles.",
    weight=3
)

# Create an instance of the expert system
career_advisor = CareerPathExpertSystem()

# Add rules to the system
career_advisor.add_rule(rule1)
career_advisor.add_rule(rule2)
career_advisor.add_rule(rule3)
career_advisor.add_rule(rule4)
career_advisor.add_rule(rule5)

# Create the GUI
root = tk.Tk()
app = CareerAdvisorGUI(root, career_advisor)
root.mainloop()

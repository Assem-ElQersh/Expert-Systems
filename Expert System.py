import tkinter as tk
from tkinter import messagebox


# Expert System Components
class ExpertSystem:
    def __init__(self):
        self.knowledge_base = []
        self.inference_engine = InferenceEngine()

    def add_rule(self, rule):
        self.knowledge_base.append(rule)

    def diagnose(self, symptoms):
        return self.inference_engine.evaluate(self.knowledge_base, symptoms)

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def matches(self, symptoms):
        return all(symptom in symptoms for symptom in self.conditions)

class InferenceEngine:
    def evaluate(self, knowledge_base, symptoms):
        for rule in knowledge_base:
            if rule.matches(symptoms):
                return rule.conclusion
        return "No diagnosis could be made due to lack of data, better to consult a doctor."

# Define rules
rule1 = Rule(["fever", "cough", "fatigue"], "Flu")
rule2 = Rule(["sneezing", "runny nose", "sore throat"], "Cold")

# Create an expert system instance
diagnosis_system = ExpertSystem()
diagnosis_system.add_rule(rule1)
diagnosis_system.add_rule(rule2)

# GUI Application
class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flu vs. Cold Diagnosis System")

        # Set up the main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Symptoms Checkboxes
        self.symptoms = {
            "fever": tk.BooleanVar(),
            "cough": tk.BooleanVar(),
            "fatigue": tk.BooleanVar(),
            "sneezing": tk.BooleanVar(),
            "runny nose": tk.BooleanVar(),
            "sore throat": tk.BooleanVar()
        }

        tk.Label(self.frame, text="Select your symptoms:").pack(anchor=tk.W)

        for symptom, var in self.symptoms.items():
            cb = tk.Checkbutton(self.frame, text=symptom.capitalize(), variable=var)
            cb.pack(anchor=tk.W)

        # Diagnose Button
        self.diagnose_button = tk.Button(self.frame, text="Diagnose", command=self.diagnose)
        self.diagnose_button.pack(pady=10)

    def diagnose(self):
        user_symptoms = [symptom for symptom, var in self.symptoms.items() if var.get()]
        diagnosis = diagnosis_system.diagnose(user_symptoms)
        messagebox.showinfo("Diagnosis", f"Diagnosis: {diagnosis}")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()

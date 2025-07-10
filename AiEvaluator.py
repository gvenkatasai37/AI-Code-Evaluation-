from transformers import pipeline

class AIEvaluator:
    def __init__(self):
        self.code_explainer = pipeline("text-generation", model="gpt-3.5-turbo")
        self.code_improver = pipeline("text-generation", model="gpt-3.5-turbo")
    
    def explain_code(self, code):
        """Generate natural language explanation of code"""
        prompt = f"Explain this Python code:\n\n{code}"
        return self.code_explainer(prompt, max_length=200)
    
    def suggest_improvements(self, code):
        """Provide code improvement suggestions"""
        prompt = f"Suggest improvements for this Python code:\n\n{code}"
        return self.code_improver(prompt, max_length=200)
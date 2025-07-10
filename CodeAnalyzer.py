import ast
from radon.complexity import cc_visit
from radon.metrics import mi_visit

class CodeAnalyzer:
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)
        
    def get_metrics(self):
        """Calculate code metrics"""
        return {
            'cyclomatic_complexity': sum(m.complexity for m in cc_visit(self.code)),
            'maintainability_index': mi_visit(self.code, True)
        }
    
    def check_style(self):
        """Run style checks"""
        # Integrate with pylint/flake8
        pass
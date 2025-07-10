from AiEvaluator import AIEvaluator
import CodeAnalyzer
from Tests import TestRunner


class CodeEvaluator:
    def __init__(self, code, test_cases=None):
        self.code = code
        self.test_cases = test_cases
        self.analyzer = CodeAnalyzer(code)
        self.ai = AIEvaluator()
        self.test_runner = TestRunner(code, test_cases) if test_cases else None
        
    def full_evaluation(self):
        """Run complete code evaluation"""
        report = {
            "metrics": self.analyzer.get_metrics(),
            "style": self.analyzer.check_style(),
            "ai_feedback": {
                "explanation": self.ai.explain_code(self.code),
                "improvements": self.ai.suggest_improvements(self.code)
            }
        }
        
        if self.test_runner:
            report["test_results"] = self.test_runner.run_tests()
            
        return report